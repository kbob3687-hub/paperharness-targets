import os
from pathlib import Path

DEVICE = "cpu" if os.environ.get("CUDA_VISIBLE_DEVICES") == "-1" else "cuda"


def main() -> None:
    if DEVICE == "cuda":
        raise RuntimeError("CUDA device not found on this machine")
    Path("out.txt").write_text(f"ran on {DEVICE}", encoding="utf-8")
    print("ran on", DEVICE)


if __name__ == "__main__":
    main()
