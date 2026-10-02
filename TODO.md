# TODO

## Fase 1: captura (en curso)
- [x] Estructura del repo, README y docs
- [x] `capture.py` y simulador `fake_device.py` (probado con el simulador)
- [ ] Comprar MPU6050 (GY-521), breadboard, jumpers y pulsador (~$15)
- [ ] Instalar CCS + MSPM0 SDK y confirmar pines I2C/GPIO libres en la guía de la LP-MSPM0G5187
- [ ] Cablear el sensor y leer `WHO_AM_I` (debe devolver 0x68)
- [ ] Firmware: transmitir muestras a 100 Hz por UART con botón (`docs/protocolo.md`)
- [ ] Probar `capture.py` con la placa real y verificar que los datos salen limpios

## Fase 2: dataset
- [ ] Grabar 4-5 clases, ≥50 repeticiones cada una, varias sesiones y velocidades
- [ ] Grabar ~20 repeticiones por clase con 2-3 personas más (solo para prueba)

## Fase 3: modelo
- [ ] Entrenar 1D-CNN, partiendo por sesión/usuario
- [ ] Cuantizar a int8, matriz de confusión, registrar precisión y tamaño

## Fase 4: inferencia y dashboard
- [ ] Confirmar en el datasheet si el MSPM0G5187 trae NPU
- [ ] Desplegar el modelo en la placa y medir latencia
- [ ] Dashboard en vivo con barras de porcentaje por clase

## Fase 5: cierre
- [ ] Llenar la tabla de métricas del README con valores medidos
- [ ] Diagrama de bloques, video de demo, repo en GitHub
- [ ] Línea del resume con cifras reales

## Opcional
- [ ] MSP430 como nodo de despertar por movimiento
- [ ] Dataset de vibración de un ventilador (mantenimiento predictivo)
- [ ] Escalar de 5 a 10 dígitos
