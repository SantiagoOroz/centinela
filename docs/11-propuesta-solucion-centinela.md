# Propuesta elegida: CENTINELA — detección temprana de jaurías en Río Grande con IA

Estado: borrador para visto bueno (12-oct-2026). Entrega: 16-oct-2026.

## 1. Por qué esta idea y no otras

Candidatas evaluadas (todas observables desde Río Grande):

| Idea | Impacto | Viabilidad | Accesibilidad | Originalidad | Evidencia local |
|---|---|---|---|---|---|
| **A. Jaurías de perros asilvestrados** (CENTINELA) | Alto: vidas, producción ovina, fauna nativa | Alta: fotos + modelos de visión existentes | Alta: WhatsApp / web simple | Alta | Muy fuerte (feb-2026, ley 1146, estudio de cámaras trampa) |
| B. Hielo en veredas: priorizar el salado con IA | Medio | Alta | Alta | Media | Débil para Río Grande (hay datos de Bariloche, no locales) |
| C. Cortes de Ruta 3 (Garibaldi / San Sebastián) | Alto | Media: depende de datos de Vialidad | Alta | Media | No encontré registros 2026 |

Se elige **A**. Gana en los tres criterios más pesados (problema 20%, solución 20%, IA 20%) y en originalidad.

## 2. El problema (qué vi, dónde, cuándo, evidencia)

- **Qué vi:** perros sueltos en grupo en los barrios del borde urbano de Río Grande (Margen Sur, Chacra XIII, zona de chacras), sin dueño visible, moviéndose hacia el campo. *(Completar con la observación personal real.)*
- **Dónde:** Río Grande, Tierra del Fuego. Periferia urbana y estancias/escuelas rurales vecinas.
- **Cuándo:** todo el año; picos en verano con las pariciones (corderos).
- **Evidencia de que no es aislado:**
  - Febrero 2026: una jauría mató más de 120 corderos de la Escuela Agrotécnica Salesiana "Nuestra Señora de la Candelaria", Río Grande. La escuela dijo que el caso se repite en distintas estancias.
  - La Asociación Rural de Tierra del Fuego pidió medidas urgentes a municipio y provincia.
  - Estudio con cámaras trampa: perros detectados en 16 de 21 estaciones, 117 individuos distintos reconocidos a mano, detecciones +226% en 5 años; hoy se los considera depredador tope del bosque fueguino.
  - Ley provincial 1146 declara al perro asilvestrado especie exótica invasora y prevé programas de control, pero casi no se aplica por falta de datos y presupuesto.
  - Lado chileno de la isla (misma geografía): 170 denuncias y cerca de 4.950 animales muertos o heridos entre 2012 y 2025, más del 80% atribuido a perros.
- **A quiénes afecta:** productores ovinos y escuelas rurales, vecinos de barrios periféricos (mordeduras, miedo a caminar), fauna nativa (guanacos, aves) y los propios perros (sufrimiento, matanzas reactivas).
- **Por qué importa:** el origen es urbano (perros con dueño que quedan sueltos en Río Grande). Si se detecta temprano, la respuesta es castración y tenencia responsable; si se detecta tarde, la única respuesta que queda es matar jaurías. Hoy nadie sabe cuántos perros hay, dónde ni cómo se mueven.

## 3. La solución: CENTINELA

Red de alerta temprana que convierte fotos (cámaras trampa + reportes vecinales) en un **mapa vivo de jaurías** y un **ranking semanal de intervención** para Zoonosis municipal y la Asociación Rural.

Tres soluciones comparadas antes de elegir:
1. Campaña de concientización + castración masiva. Cambia conductas, pero a ciegas: no sabe dónde intervenir primero.
2. Cercos eléctricos y perros guardianes en estancias. Protege a quien puede pagarlos; no resuelve el origen urbano.
3. **CENTINELA** (elegida): datos + IA para dirigir las acciones de 1 y 2 a donde más importa, con bajo costo.

## 4. Rol concreto de la IA

| Pregunta | Respuesta |
|---|---|
| Tarea | (a) Visión por computadora: detectar perros en fotos de cámaras trampa y de vecinos, y **re-identificar individuos** (pelaje, tamaño, marcas) para contar perros reales y no detecciones repetidas. (b) Agrupar detecciones en jaurías y zonas calientes. (c) Lenguaje natural: leer reportes de WhatsApp/Facebook ("vi 5 perros en la Chacra II a las 7") y convertirlos en registros con lugar, hora y cantidad. (d) Modelo de riesgo: cruzar jaurías, estancias, escuelas y época de parición para predecir riesgo de ataque por zona. |
| Información | Fotos con fecha y GPS, reportes de texto, mapa de estancias/escuelas/barrios, calendario de pariciones, registro de perros castrados/con chip. |
| Resultado | Mapa de calor + ficha por jauría (cuántos, dónde, desde cuándo) + lista semanal priorizada: dónde castrar, qué estancias alertar, qué perros parecen tener dueño (collar) y volver al barrio. |
| Quién revisa | Zoonosis de la Municipalidad de Río Grande y la Asociación Rural; investigadores (CADIC/INTA) validan las identificaciones. La IA propone, las personas deciden. |
| Por qué la IA hace mejor la solución | Los investigadores tardaron años en identificar 117 perros a mano. La IA lo hace en minutos y de forma continua; además lee cientos de reportes informales que hoy se pierden en grupos de WhatsApp. Sin IA no hay mapa; sin mapa no hay prevención, solo reacción. |

Ética: no identifica personas, no recomienda matar animales, prioriza castración y devolución de perros con dueño; datos de vecinos anónimos; validación humana obligatoria.

## 5. Recorrido paso a paso

1. **Activación:** un vecino manda foto o texto al WhatsApp de CENTINELA; una cámara trampa sube su foto automáticamente; un productor reporta un ataque.
2. **Ingesta:** el sistema guarda la imagen/texto con fecha y ubicación.
3. **IA, visión:** detecta perros y re-identifica individuos; descarta repetidos.
4. **IA, lenguaje:** convierte reportes de texto en registros estructurados.
5. **IA, análisis:** agrupa en jaurías, calcula zonas calientes y riesgo semanal.
6. **Revisión humana:** Zoonosis valida el tablero (confirma, corrige o descarta).
7. **Salida:** tablero web para municipio y Asociación Rural; alerta de WhatsApp a estancias y escuelas en zona de riesgo; informe mensual público.
8. **Acción:** operativos de castración y recuperación de perros con dueño en los barrios de origen; refuerzo de guardia en estancias alertadas.
9. **Aprendizaje:** cada acción se registra; el modelo mejora su ranking.

Responsables: vecinos y productores (reportan), equipo CENTINELA (sistema), Zoonosis municipal (decide), Asociación Rural y escuelas (reciben alertas), CADIC/INTA (validan la ciencia).

## 6. Viabilidad e impacto

- Tecnología existente: modelos abiertos de detección (YOLO) y re-identificación de animales (ya usados con cámaras trampa); un LLM para los reportes; WhatsApp Business; mapa web.
- Costo inicial bajo: cámaras trampa ya instaladas por investigadores; celulares de vecinos.
- Aliados naturales: Municipalidad de Río Grande (Zoonosis), Asociación Rural de TDF, CADIC, Escuela Agrotécnica Salesiana.
- Escalable a toda la isla (incluido el lado chileno, con el mismo problema) y a cualquier región ganadera con perros asilvestrados en América.
- Métricas: perros identificados, jaurías mapeadas, castraciones dirigidas, ataques por temporada, corderos perdidos.

## 7. Formato de entrega recomendado

**Diseño visual: 6 slides en PDF** (categoría "Diseño visual"). Permite mostrar mapa, mockups y flujo; compite solo con otras propuestas visuales (3 finalistas por formato).

Slides:
1. Portada: CENTINELA + una frase + Río Grande.
2. El problema con evidencia (120 corderos, 117 perros, +226%, ley 1146).
3. A quiénes afecta y por qué importa (origen urbano → prevención).
4. La solución y el flujo paso a paso.
5. Qué hace la IA (visión + lenguaje + riesgo) y por qué sin IA no funciona; ética.
6. Mockup del tablero (MVP) + viabilidad, aliados, impacto, escalabilidad.

Además se construye un **MVP web interactivo** (mapa simulado de Río Grande, detecciones ficticias, ficha de jauría, ranking semanal) cuyas capturas van en las slides.

Archivo: `Santiago Oroz_Argentina_Diseño visual_#AIforImpact2026.pdf`

## Fuentes
- https://www.noticiasnqn.com.ar/noticias/2026/02/09/327913-una-jauria-de-perros-salvajes-mato-a-mas-de-120-ovejas-en-una-escuela-agrotecnica-de-rio-grande
- https://www.diariodecuyo.com.ar/argentina/una-jauria-de-perros-salvajes-mato-a-mas-de-100-corderos-de-una-escuela-rural-1829936.html
- https://bichosdecampo.com/otra-vez-atacaron-los-perros-salvajes-de-tierra-de-fuego-a-la-reconocida-escuela-salesiana-de-rio-grande-le-mataron-mas-de-120-corderos-y-muchos-suenos/
- https://bichosdecampo.com/los-capos-de-los-bosques-australes-la-deteccion-de-perros-asilvestrados-en-tierra-del-fuego-crecio-226-en-5-anos-y-ya-son-considerados-depredadores-apice/
- https://www.theclinic.cl/2026/08/28/quien-se-hace-cargo-corte-rechaza-recurso-interpuesto-por-ganaderos-para-frenar-las-miles-de-muertes-que-generan-perros-asilvestrados-en-tierra-del-fuego/
- https://www.diarioconstitucional.cl/2026/07/23/ganaderos-recurren-por-ataques-de-jaurias-que-han-causado-millonarias-perdidas-en-tierra-del-fuego/
