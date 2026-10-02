# Protocolo UART (firmware → PC)

Texto ASCII, una línea por mensaje, terminada en `\n`. Se usa el puerto serial virtual que la LaunchPad expone por USB (backchannel del XDS110). Velocidad: **115200 baudios, 8N1**.

Es texto a propósito: se depura con cualquier monitor serial y no hace falta un parser binario en esta fase. Si la tasa de datos no alcanza, se pasa a binario después.

## Mensajes

| Mensaje | Cuándo se envía |
|---------|-----------------|
| `READY` | Al arrancar, una vez |
| `START` | Cuando se presiona el botón (empieza el gesto) |
| `ax,ay,az,gx,gy,gz` | Una por muestra mientras el botón esté presionado. Enteros crudos de 16 bits con signo, tal como salen del MPU6050 |
| `END` | Cuando se suelta el botón |

Ejemplo:

```
READY
START
-312,16204,1020,-45,12,7
-298,16190,1034,-40,15,9
...
END
```

## Parámetros del sensor (fijar en el firmware)

- Frecuencia de muestreo: **100 Hz**
- Rango del acelerómetro: ±4 g (sensibilidad 8192 LSB/g)
- Rango del giroscopio: ±500 °/s (sensibilidad 65.5 LSB/(°/s))
- Filtro pasa-bajas digital del MPU6050 (DLPF): ~44 Hz

## Presupuesto de ancho de banda

Una línea tiene unos 30-40 caracteres. A 100 Hz son ~4 KB/s, y 115200 baudios dan ~11.5 KB/s, así que alcanza con margen. Si subes la frecuencia o añades campos, súbele también los baudios.

## Respuesta de inferencia (Fase 4)

Cuando el modelo corra en la placa, tras `END` el firmware enviará:

```
RESULT,<clase_ganadora>,<p0>,<p1>,...,<pN>
```

con las probabilidades como enteros 0-100. Esto se define con detalle en la Fase 4.
