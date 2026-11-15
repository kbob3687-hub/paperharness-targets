from pathlib import Path


def main() -> None:
    values = [i * i for i in range(10)]
    Path("out.txt").write_text(",".join(map(str, values)), encoding="utf-8")
    print("sum =", sum(values))


if __name__ == "__main__":
    main()
