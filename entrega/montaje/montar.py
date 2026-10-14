# Arma el video final: pantalla (re-sincronizada a tu voz) + efectos + tu voz + tu cámara + subtítulos.
# Uso:
#   python montar.py                 -> video final completo
#   python montar.py --prueba 95 20  -> solo 20 s desde el segundo 95, rápido y en baja calidad (para probar ajustes)
# Todo lo ajustable está en montaje.json y subtitulos.srt.
import json, os, shutil, subprocess, sys
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
os.chdir(AQUI)
CFG = json.load(open("montaje.json", encoding="utf-8"))
EV = json.load(open("eventos.json", encoding="utf-8"))["events"]

GYAN = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe")
FF = GYAN if os.path.exists(GYAN) else shutil.which("ffmpeg")

prueba = None
if "--prueba" in sys.argv:
    i = sys.argv.index("--prueba"); prueba = (float(sys.argv[i + 1]), float(sys.argv[i + 2]))

# ---------- mapa de tiempo: segundo del video de pantalla -> segundo del video final ----------
anclas = sorted(CFG["anclas"], key=lambda a: a["pantalla"])
P = [a["pantalla"] for a in anclas]; V = [a["voz"] for a in anclas]
def mapear(t):
    for k in range(len(P) - 1):
        if t <= P[k + 1] or k == len(P) - 2:
            return V[k] + (t - P[k]) * (V[k + 1] - V[k]) / (P[k + 1] - P[k])

DUR = CFG["duracion_final"]

# ---------- máscara y aro de la cámara ----------
cam = CFG["camara"]; D = cam["diametro"]; B = cam["borde"]
def forma(draw, box, fill):
    if cam["forma"] == "circulo": draw.ellipse(box, fill=fill)
    else: draw.rounded_rectangle(box, radius=cam.get("radio_esquinas", 28), fill=fill)
m = Image.new("L", (D * 4, D * 4), 0); forma(ImageDraw.Draw(m), (0, 0, D * 4 - 1, D * 4 - 1), 255)
m.resize((D, D), Image.LANCZOS).save("_mascara.png")
R = D + 2 * B
r = Image.new("RGBA", (R * 4, R * 4), (0, 0, 0, 0)); forma(ImageDraw.Draw(r), (0, 0, R * 4 - 1, R * 4 - 1), tuple(int(cam["color_borde"][i:i + 2], 16) for i in (1, 3, 5)) + (255,))
r.resize((R, R), Image.LANCZOS).save("_aro.png")

def xy(pos):
    mg = cam["margen"]
    x = mg if "izq" in pos else 1920 - R - mg
    y = mg if "arriba" in pos else 1080 - R - mg - cam.get("subir", 0)
    return x, y
tramos = sorted(cam["posiciones"], key=lambda p: p["desde"])
def expr(idx):
    e = str(xy(tramos[-1]["pos"])[idx])
    for p in reversed(tramos[:-1]):
        nxt = tramos[tramos.index(p) + 1]["desde"]
        e = f"if(lt(t,{nxt}),{xy(p['pos'])[idx]},{e})"
    return e

# ---------- entradas ----------
inp = []; f = []
def entrada(*a):
    inp.extend(a); return sum(1 for x in inp if x == "-i") - 1

ip = entrada("-i", "pantalla.mp4")
iv = entrada("-ss", str(CFG["voz_recorte_inicio"]), "-i", CFG["voz"])
ic = entrada("-ss", str(CFG["voz_recorte_inicio"] + CFG["camara_desfase"]), "-i", CFG["camara_video"])
im = entrada("-loop", "1", "-i", "_mascara.png")
ia = entrada("-loop", "1", "-i", "_aro.png")
ib = entrada("-stream_loop", "-1", "-i", "sfx/bed.wav")

# pantalla: cada tramo entre anclas se acelera/frena para caer donde hablás
segs = []
for k in range(len(P) - 1):
    a, b = P[k], P[k + 1]
    f.append(f"[{ip}:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)*{(V[k+1]-V[k])/(b-a):.5f}[p{k}]"); segs.append(f"[p{k}]")
f.append("".join(segs) + f"concat=n={len(segs)}:v=1:a=0,fps=30,tpad=stop_mode=clone:stop_duration=10,trim=0:{DUR},setpts=PTS-STARTPTS[pant]")

# cámara recortada en círculo con aro
cx, cy, lado = cam["recorte_cara"]
f.append(f"[{ic}:v]fps=30,crop={lado}:{lado}:{cx - lado // 2}:{cy - lado // 2},scale={D}:{D},format=rgba[c0]")
f.append(f"[{im}:v]format=gray,scale={D}:{D}[mk]")
f.append(f"[c0][mk]alphamerge,fade=t=in:st=0:d=0.6:alpha=1[c1]")
f.append(f"[{ia}:v]format=rgba,fade=t=in:st=0:d=0.6:alpha=1[aro]")
f.append(f"[pant][aro]overlay=x='{expr(0)}':y='{expr(1)}':shortest=1[v1]")
f.append(f"[v1][c1]overlay=x='{expr(0)}+{B}':y='{expr(1)}+{B}':shortest=1[v2]")

# subtítulos
s = CFG["subtitulos"]
estilo = (f"FontName={s['fuente']},FontSize={s['tamano']},PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
          f"BackColour=&H{s['opacidad_fondo']:02X}000000,BorderStyle=4,Outline=0,Shadow=0,Bold=1,Alignment=2,"
          f"MarginV={s['margen_abajo']},MarginL={s['margen_izq']},MarginR={s['margen_der']}")
if s.get("activados", True):
    f.append(f"[v2]subtitles={s['archivo']}:original_size=1920x1080:force_style='{estilo}'[vout]")
else:
    f.append("[v2]null[vout]")

# audio: voz + música de fondo + efectos re-ubicados
vol = CFG["volumen"]
mix = []
f.append(f"[{iv}:a]atrim=0:{DUR},asetpts=PTS-STARTPTS,volume={vol['voz']}[voz]"); mix.append("[voz]")
f.append(f"[{ib}:a]atrim=0:{DUR},afade=t=in:d=1.5,afade=t=out:st={DUR-2}:d=2,volume={vol['musica']}[bed]"); mix.append("[bed]")
sfx = {"scene": ("whoosh.wav", -0.15, vol["whoosh"]), "click": ("click.wav", 0.0, vol["click"]), "toast": ("ding.wav", 0.1, vol["ding"])}
for e in EV:
    if e["kind"] not in sfx: continue
    archivo, corr, v = sfx[e["kind"]]
    t = max(0.0, mapear(e["out_t"]) + corr)
    if t >= DUR - 0.2: continue
    n = entrada("-i", f"sfx/{archivo}")
    f.append(f"[{n}:a]adelay={int(t*1000)}:all=1,volume={v}[s{n}]"); mix.append(f"[s{n}]")
f.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")

salida = CFG["salida"]
cmd = [FF, "-y", "-v", "error", "-stats"] + inp + ["-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]"]
if prueba:
    salida = "_prueba.mp4"
    cmd += ["-ss", str(prueba[0]), "-t", str(prueba[1]), "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28"]
else:
    cmd += ["-t", str(DUR), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p"]
cmd += ["-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", salida]
print("Renderizando", salida, "...")
subprocess.check_call(cmd)
print("Listo:", os.path.abspath(salida))
