# CENTINELA · Guion de presentación y checklist de entrega

## Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| `Santiago Oroz_Argentina_Video_#AIforImpact2026.mp4` | **El entregable recomendado.** Video de 2:57, 1920x1080, con narración (voz sintética) y efectos. |
| `Santiago Oroz_Argentina_Video_#AIforImpact2026 (solo efectos, para poner tu voz).mp4` | Mismo video sin voz: para grabar tu propia narración encima (ver `guion-video.md`). |
| `guion-video.md` | Guion del video con marcas de tiempo por escena, para grabar tu voz. |
| `Santiago Oroz_Argentina_Diseño visual_#AIforImpact2026.pdf` | Alternativa en formato Diseño visual: 6 slides 16:9. Entregá **uno solo** de los dos formatos. |
| `centinela-deck.html` | Fuente de las slides. Si cambiás texto, regenerá el PDF (ver abajo). |
| `preview/s1..s6.png` | Vista previa de cada slide. |
| `../mvp/centinela.html` | MVP interactivo. Abrilo en el navegador para mostrarlo a 1 o 2 personas (actividad de la cápsula 5). |
| `../capturas/` | Capturas del MVP usadas en la slide 6. |
| `../docs/11-propuesta-solucion-centinela.md` | Respuestas completas a las actividades de las cápsulas 1 a 4 (observación, 3 soluciones, rol de la IA, mapa paso a paso). |

## Antes de subir (checklist del reglamento)

- [ ] Nombre ya puesto: Santiago Oroz (portada y nombre del archivo).
- [ ] Ajustar en la slide 2 la observación personal si viste los perros en otro barrio u horario (sé concreto: barrio, hora, cuántos).
- [ ] Regenerar el PDF si tocaste `centinela-deck.html` (comando abajo).
- [ ] Elegir **un solo formato**: video (recomendado) o PDF. El reglamento no acepta propuestas en más de un formato.
- [ ] Si es video: MP4, menos de 3 min (dura 2:57), 1920x1080, menos de 500 MB (pesa unos 27 MB), con audio. Si grabaste tu voz, exportá con el mismo nombre.
- [ ] Si es PDF: 6 slides, menos de 20 MB (hoy pesa unos 7 MB).
- [ ] Subir a Google Drive o Dropbox. Permiso: **"Cualquier persona con el enlace puede ver"**. Probar el link en una ventana de incógnito: no debe pedir login.
- [ ] Nombre exacto del archivo en Drive: `Santiago Oroz_Argentina_Video_#AIforImpact2026` (o `..._Diseño visual_...` si entregás el PDF).
- [ ] Completar las 6 cápsulas en Moodle y pegar el link en el formulario de entrega **antes del 16 de octubre de 2026**.
- [ ] El link de Drive debe apuntar al archivo elegido, no a una carpeta con varios. El MVP vive aparte en https://santiagooroz.github.io/centinela/ (repo github.com/SantiagoOroz/centinela, solo con tu cuenta) y está enlazado con QR en la slide 6 y al final del video.

## Regenerar el PDF

Desde la carpeta `entrega`, en PowerShell:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=20000 --print-to-pdf="$PWD\Santiago Oroz_Argentina_Diseño visual_#AIforImpact2026.pdf" "file:///$($PWD -replace '\\','/')/centinela-deck.html"
```

## Guion de 3 minutos (por si lo presentás en voz alta o te lo preguntan en mentoría)

**Slide 1 (10 s).** CENTINELA es una red de alerta temprana con IA para frenar las jaurías de perros asilvestrados en Río Grande antes de que ataquen.

**Slide 2 (40 s).** En los barrios del borde de la ciudad veo grupos de perros sin dueño que de madrugada salen al campo. En febrero una jauría mató más de 120 corderos de la Escuela Agrotécnica, a minutos de la ciudad. No es un caso aislado: un estudio con cámaras trampa identificó a mano 117 perros distintos y las detecciones crecieron 226% en cinco años.

**Slide 3 (35 s).** Afecta a productores y escuelas rurales, a los vecinos de la periferia, a la fauna nativa y a los propios perros. El origen es urbano: un perro con dueño queda suelto, se junta con otros y termina en el campo. Hay una ley provincial, la 1146, pero no se aplica porque falta lo básico: saber cuántos perros hay, dónde están y de qué barrio salen.

**Slide 4 (35 s).** CENTINELA recibe fotos de cámaras trampa y mensajes de vecinos por WhatsApp. La IA los procesa y arma un mapa vivo de jaurías y un ranking de intervención. Zoonosis municipal y la Asociación Rural validan y deciden: alertar estancias y escuelas, castrar y devolver perros con dueño en el barrio de origen.

**Slide 5 (40 s).** La IA hace tres cosas que nadie puede hacer a mano: visión por computadora para reconocer a cada perro individual en cada foto; lenguaje natural para convertir mensajes informales en datos; y un modelo de riesgo que anticipa dónde puede haber un ataque esta semana. Sin IA, identificar 117 perros llevó años. Con IA, es continuo y en minutos. La IA propone, las personas deciden. No identifica personas ni recomienda matar animales.

**Slide 6 (20 s).** Ya hay un MVP interactivo que muestra el recorrido completo. Es viable con modelos abiertos y cámaras que ya existen; sería viable con aliados locales como Zoonosis municipal, la Asociación Rural y el CADIC, a quienes este problema ya les preocupa; y escala a toda la isla y a cualquier región ganadera de América.

## Preguntas para probar el MVP con 1 o 2 personas (cápsula 5)

Mostrá `centinela.html` sin explicar nada y preguntá:
1. ¿Qué problema resuelve?
2. ¿Cómo funciona?
3. ¿Qué hace la IA?
4. ¿Qué parte no se entiende con claridad?

Anotá las respuestas: si algo no se entiende, se ajusta el texto de la slide 4 o 5.

## Fuentes citadas en la slide 2
- Noticias NQN (09-feb-2026): jauría mató más de 120 ovejas en la escuela agrotécnica de Río Grande.
- Diario de Cuyo (07-feb-2026): más de 100 corderos muertos en una escuela rural.
- Bichos de Campo: estudio con cámaras trampa, 117 individuos, +226% en 5 años; pedido de la Asociación Rural de TDF.
- The Clinic (28-ago-2026) y Diario Constitucional (23-jul-2026): cifras del lado chileno (170 denuncias, cerca de 4.950 animales, más del 80% por perros).
- Ley provincial 1146 de Tierra del Fuego.
