from pathlib import Path

DATASET = Path("data/private/dataset.csv")


def main() -> None:
    if not DATASET.exists():
        raise FileNotFoundError(
            "dataset not found: private dataset.csv must be copied from internal storage"
        )
    rows = DATASET.read_text(encoding="utf-8").strip().splitlines()
    Path("out.txt").write_text(str(len(rows)), encoding="utf-8")
    print("rows", len(rows))


if __name__ == "__main__":
    main()
