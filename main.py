from pathlib import Path

INPUT = Path("/data/paperharness_input.csv")
OUTPUT = Path("/tmp/paperharness_out.txt")


def main() -> None:
    rows = INPUT.read_text(encoding="utf-8").strip().splitlines()
    total = sum(float(row.split(",")[1]) for row in rows[1:])
    OUTPUT.write_text(str(total), encoding="utf-8")
    print("total", total)


if __name__ == "__main__":
    main()
