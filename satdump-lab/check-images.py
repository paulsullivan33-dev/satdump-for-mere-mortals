#!/usr/bin/env python3
"""Check the products of a SatDump NOAA APT decode without needing eyes.

For each PNG in a decode output directory this prints the image size,
mode, and the 16-bit pixel range/percentiles -- enough to show the file
holds a real picture (a wide spread of values, structure in the
percentiles) rather than a blank or saturated frame. It also checks the
APT line arithmetic: an APT recording of N seconds should produce very
close to 2*N lines, since APT sends exactly 2 lines per second.

Usage: check-images.py OUTPUT_DIR RECORDING_SECONDS
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image


def main() -> None:
    out = Path(sys.argv[1])
    seconds = float(sys.argv[2])
    print(f"recording length: {seconds:.1f} s -> expected APT lines ~{2 * seconds:.0f}")
    for path in sorted(out.glob("*.png")):
        im = Image.open(path)
        a = np.asarray(im).astype(np.float64)
        print(
            f"{path.name:48s} {str(im.size):14s} mode={im.mode:4s} "
            f"min={a.min():7.0f} max={a.max():7.0f} "
            f"p1={np.percentile(a, 1):7.0f} p99={np.percentile(a, 99):7.0f}"
        )
    ds = out / "dataset.json"
    if ds.exists():
        print("\ndataset.json:")
        print(ds.read_text())


if __name__ == "__main__":
    main()
