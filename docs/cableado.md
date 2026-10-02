# Cableado y compra

## Lista de compra (~$15)

- Módulo MPU6050 (GY-521), con pines ya soldados
- Breadboard pequeño
- Jumpers hembra-hembra y macho-hembra
- Un pulsador (cualquier tipo de 4 patas sirve)

## Conexiones

Alimenta el MPU6050 a **3.3 V**, que es el nivel lógico de la LaunchPad. Muchos módulos GY-521 traen regulador y aceptan 5 V, pero conectado a 3.3 V no hay riesgo para los pines de la placa.

| MPU6050 | LaunchPad MSPM0G5187 |
|---------|----------------------|
| VCC | 3V3 |
| GND | GND |
| SCL | pin I2C SCL |
| SDA | pin I2C SDA |
| AD0 | GND (dirección I2C 0x68) |

| Botón | LaunchPad |
|-------|-----------|
| Pata 1 | GPIO de entrada (con pull-up interno) |
| Pata 2 | GND |

**Los números de pin exactos hay que confirmarlos** en la guía de usuario de la LP-MSPM0G5187 y en el pinmux de SysConfig (en Code Composer Studio). Escoge un módulo I2C y un GPIO que no estén ocupados por los LEDs o botones de la placa. No los asumas.

## Revisión rápida antes de energizar

1. VCC y GND no están invertidos.
2. SDA y SCL no están intercambiados.
3. Cables firmes en el breadboard (un cable flojo se ve como datos que se cortan).
4. Primera prueba: lee el registro `WHO_AM_I` (0x75) del MPU6050. Debe devolver `0x68`. Si no, revisa cableado y dirección antes de seguir.

## Dónde sujetar el sensor

Para dibujar números en el aire, fija el sensor a la mano o a un objeto pequeño (un bolígrafo con cinta). Mantén **siempre la misma orientación** al grabar: si giras el sensor entre sesiones, el modelo lo va a ver como un gesto distinto.
