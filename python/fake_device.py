#!/usr/bin/env python3
"""Simula la placa para probar capture.py sin hardware.

Crea un par de puertos seriales virtuales (pty) y envía gestos falsos con el
protocolo de docs/protocolo.md. Solo Linux/macOS.

Uso:
    python fake_device.py            # imprime la ruta del puerto virtual
    python capture.py --port <ruta> --label 3 --count 3
"""
import math
import os
import pty
import random
import time


def fake_gesture(n=150):
    phase = random.uniform(0, math.pi)
    for i in range(n):
        t = i / n
        ax = int(3000 * math.sin(2 * math.pi * t + phase) + random.gauss(0, 80))
        ay = int(16000 + 2000 * math.cos(2 * math.pi * t) + random.gauss(0, 80))
        az = int(1000 + 1500 * math.sin(4 * math.pi * t) + random.gauss(0, 80))
        gx, gy, gz = (int(random.gauss(0, 200)) for _ in range(3))
        yield f"{ax},{ay},{az},{gx},{gy},{gz}"


def main():
    master, slave = pty.openpty()
    print(os.ttyname(slave), flush=True)
    os.write(master, b"READY\n")
    while True:
        time.sleep(1.0)
        os.write(master, b"START\n")
        for line in fake_gesture():
            os.write(master, (line + "\n").encode())
            time.sleep(0.01)
        os.write(master, b"END\n")


if __name__ == "__main__":
    main()
