# Dataset

## Qué se graba

Un archivo CSV por gesto en `data/raw/`. Nombre:

```
<etiqueta>_<usuario>_<sesion>_<n>.csv
ej.  3_jorge_s01_007.csv
```

Contenido: encabezado `t_ms,ax,ay,az,gx,gy,gz`, donde `t_ms` es el tiempo en milisegundos desde el inicio del gesto (calculado en la PC) y el resto son los valores crudos del sensor.

## Protocolo de captura (importante para que el modelo generalice)

- **≥50 repeticiones por clase** para empezar. Más es mejor.
- **Varía** velocidad (lento, normal, rápido) y tamaño del dígito (pequeño, grande) entre repeticiones.
- **Varias sesiones** en días distintos, no todas seguidas. Un modelo entrenado y probado en la misma sesión da una precisión inflada.
- **Orientación del sensor constante** en todas las sesiones.
- **Otras personas**: pide a 2-3 amigos que graben ~20 repeticiones por clase con un `usuario` distinto. Para evaluar, reserva sus datos solo para prueba. Esa cifra es la que vale en el resume.
- Duración típica de un gesto: 1-2 s (100-200 muestras).

## Partición para evaluar

Separa por **sesión o por usuario**, no por muestra al azar. Si mezclas repeticiones de la misma sesión entre entrenamiento y prueba, el modelo ve casi los mismos datos y la precisión sale falsamente alta.

Propuesta:
- Entrenamiento: tus sesiones 1 a N-1
- Validación: tu última sesión
- Prueba final: los datos de otras personas

## Qué no subir a git

Si el dataset crece, agrégalo a `.gitignore` y publica un ZIP aparte o un enlace. Sí sube un puñado de ejemplos pequeños para que el repo se pueda probar.
