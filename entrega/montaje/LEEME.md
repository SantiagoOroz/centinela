# Montaje del video final

`montar.py` junta la pantalla, los efectos, tu voz, tu cámara y los subtítulos. Todo lo que se ajusta está en `montaje.json` y `subtitulos.srt`.

## Probar rápido un tramo (unos 10 s de espera)

```
python montar.py --prueba 95 20
```

Genera `_prueba.mp4` con 20 segundos a partir del segundo 95 del video final. Abrilo, corregí y repetí.

## Render final (unos 4 min)

```
python montar.py
```

Lo escribe en `../Santiago Oroz_Argentina_Video_#AIforImpact2026.mp4`. Tiene que durar menos de 3:00, así que `duracion_final` no puede pasar de 179.9.

## Qué tocar en montaje.json

- **`anclas`**: es lo principal para sincronizar. Cada escena del video de pantalla (`pantalla`) cae en el segundo de tu voz que indica `voz`. Entre dos anclas, el video se acelera o se frena solo, y los clicks y efectos se mueven con él.
  - Si una escena aparece **tarde** respecto de lo que decís, bajá su `voz`. Si aparece **temprano**, subila.
  - No toques `pantalla`, salvo que agregues un ancla nueva. Los segundos de cada click y zoom del video de pantalla están en `eventos.json` (`out_t`).
- **`camara_desfase`**: sincroniza tu cara con tu voz (lo calculé por el movimiento de labios: 0.45). Si tus labios van atrasados respecto de la voz, subilo de a 0.1. Si van adelantados, bajalo.
- **`voz_recorte_inicio`**: recorta segundos del inicio de tu voz, y la cámara lo sigue.
- **`camara.posiciones`**: dónde está tu cámara y desde qué segundo. Valores posibles: `abajo-der`, `abajo-izq`, `arriba-der` y `arriba-izq`. Por ejemplo:
  `[{"desde": 0, "pos": "abajo-der"}, {"desde": 167, "pos": "arriba-der"}]`
- **`camara.forma`**: `circulo` o `cuadrado` (cuadrado con esquinas redondeadas, según `radio_esquinas`). `diametro` es el tamaño en píxeles y `recorte_cara` es `[centro x, centro y, lado]` dentro de tu grabación de 1280x720.
- **`subtitulos`**: `tamano` (13 ≈ 49 px), `margen_der` (deja lugar a la cámara) y `activados`.
- **`volumen`**: voz, música, whoosh, click y ding.

## subtitulos.srt

Es texto plano: se edita con el Bloc de notas. Cada bloque tiene un número, `inicio --> fin` y el texto. Los tiempos son de tu voz, que coinciden con el video final.

## Archivos

- `pantalla.mp4`: grabación del deck y del MVP, sin audio.
- `eventos.json`: segundos de escenas, clicks y zooms en `pantalla.mp4`.
- `sfx/`: efectos (`click.wav` es el click nuevo).
