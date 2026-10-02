#!/usr/bin/env python3
"""Captura gestos etiquetados desde la LaunchPad por puerto serial.

Uso:
    python capture.py --port /dev/ttyACM0 --label 3 --user jorge --session s01
    python capture.py --port COM5 --label 3 --user jorge --session s01 --count 50

Cada gesto (de START a END) se guarda como un CSV en data/raw/.
Protocolo: ver docs/protocolo.md
"""
import argparse
import csv
import sys
import time
from pathlib import Path

import serial  # pyserial

SAMPLE_PERIOD_MS = 10  # 100 Hz, debe coincidir con el firmware
MIN_SAMPLES = 30       # descarta gestos demasiado cortos (rebote del botón)
MAX_SAMPLES = 400      # descarta gestos demasiado largos (botón atascado)
HEADER = ["t_ms", "ax", "ay", "az", "gx", "gy", "gz"]


def parse_sample(line: str):
    """Devuelve una lista de 6 enteros, o None si la línea no es una muestra válida."""
    parts = line.split(",")
    if len(parts) != 6:
        return None
    try:
        return [int(p) for p in parts]
    except ValueError:
        return None


def next_index(out_dir: Path, label: str, user: str, session: str) -> int:
    prefix = f"{label}_{user}_{session}_"
    existing = [p.stem.rsplit("_", 1)[-1] for p in out_dir.glob(prefix + "*.csv")]
    nums = [int(n) for n in existing if n.isdigit()]
    return max(nums, default=0) + 1


def save_gesture(path: Path, samples):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        for i, s in enumerate(samples):
            w.writerow([i * SAMPLE_PERIOD_MS, *s])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", required=True, help="puerto serial (COM5, /dev/ttyACM0, ...)")
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--label", required=True, help="etiqueta del gesto, ej. 3")
    ap.add_argument("--user", default="jorge")
    ap.add_argument("--session", default="s01")
    ap.add_argument("--count", type=int, default=0, help="parar tras N gestos válidos (0 = hasta Ctrl+C)")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "data" / "raw"))
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    idx = next_index(out_dir, args.label, args.user, args.session)

    ser = serial.Serial(args.port, args.baud, timeout=1)
    print(f"Escuchando en {args.port}. Etiqueta '{args.label}'. Mantén el botón y dibuja el número. Ctrl+C para salir.")

    saved = 0
    recording = False
    samples = []
    try:
        while args.count == 0 or saved < args.count:
            raw = ser.readline()
            if not raw:
                continue
            line = raw.decode("ascii", errors="ignore").strip()
            if line == "START":
                recording, samples = True, []
            elif line == "END" and recording:
                recording = False
                n = len(samples)
                if MIN_SAMPLES <= n <= MAX_SAMPLES:
                    path = out_dir / f"{args.label}_{args.user}_{args.session}_{idx:03d}.csv"
                    save_gesture(path, samples)
                    idx += 1
                    saved += 1
                    print(f"[{saved}] guardado {path.name} ({n} muestras)")
                else:
                    print(f"descartado: {n} muestras (esperado {MIN_SAMPLES}-{MAX_SAMPLES})")
            elif recording:
                s = parse_sample(line)
                if s is not None:
                    samples.append(s)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()
    print(f"Listo. {saved} gestos guardados en {out_dir}")


if __name__ == "__main__":
    sys.exit(main())
