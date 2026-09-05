from pathlib import Path
import os

# Maximum amount of disk space to use, in GB
LIMIT_GB = 1

folder = Path("waste_data")
folder.mkdir(exist_ok=True)

target_bytes = LIMIT_GB * 1024**3
written = 0

chunk = os.urandom(1024 * 1024)  # 1 MB

try:
    while written < target_bytes:
        remaining = target_bytes - written
        data = chunk[:min(len(chunk), remaining)]

        with open(folder / f"junk_{written // (1024**2)}.bin", "wb") as f:
            f.write(data)

        written += len(data)
        print(f"Wrote {written / 1024**3:.2f} GB")

    print(f"Done. Used approximately {LIMIT_GB} GB.")

except KeyboardInterrupt:
    print("\nStopped by user.")
