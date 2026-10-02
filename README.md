# Números en el aire: reconocimiento de gestos con IMU y edge AI

Reconocimiento de dígitos dibujados en el aire usando un acelerómetro/giroscopio (MPU6050) y una red neuronal pequeña que corre en un microcontrolador TI MSPM0G5187 (LaunchPad `LP-MSPM0G5187`). Un dashboard en Python muestra la probabilidad por clase en tiempo real (ej. 90% "3", 10% "5").

> Estado: **Fase 1** (captura de datos). Las métricas de abajo se llenan a medida que avanza el proyecto. No pongas números en el resume que no hayas medido.

## Arquitectura

```
 MPU6050 --I2C--> MSPM0G5187 --UART (USB/XDS110)--> PC
 + botón          (firmware C:                        capture.py -> dataset
                   lectura + inferencia)              dashboard.py -> barras de %
```

Una sola placa. El MSP430FR2355 queda como extensión opcional (nodo de bajo consumo que despierta al MSPM0 al detectar movimiento).

## Fases

| Fase | Entregable | Estado |
|------|-----------|--------|
| 1 | Cableado + firmware que transmite muestras crudas + `capture.py` | en curso |
| 2 | Dataset propio (≥50 repeticiones por clase, varias velocidades y tamaños) | pendiente |
| 3 | Entrenamiento (1D-CNN), cuantización int8, evaluación | pendiente |
| 4 | Inferencia en el MSPM0 + dashboard en vivo | pendiente |
| 5 | README final, diagrama, video de demo | pendiente |
| Extra | MSP430 como nodo de despertar / dataset de vibración de ventilador | opcional |

Empieza con 4-5 clases (por ejemplo 0, 1, 2, 3, 5). Escala a 10 cuando tengas algo que funcione.

## Métricas para el resume (llenar con valores medidos)

| Métrica | Valor |
|---------|-------|
| Clases | |
| Muestras de entrenamiento / prueba | |
| Precisión en prueba (tú) | |
| Precisión con otras personas | |
| Tamaño del modelo (int8) | |
| Latencia de inferencia en el MSPM0 | |
| Consumo promedio | |

## Estructura

```
numeros-aire/
├── README.md
├── docs/
│   ├── cableado.md     # conexiones y compra
│   ├── protocolo.md    # formato UART entre firmware y PC
│   └── dataset.md      # formato de datos y protocolo de captura
├── firmware/           # proyecto de Code Composer Studio (Fase 1 en adelante)
├── python/
│   ├── capture.py      # graba gestos etiquetados
│   ├── requirements.txt
│   └── fake_device.py  # simula la placa para probar sin hardware
└── data/raw/           # CSV por gesto (no se sube a git si crece mucho)
```
