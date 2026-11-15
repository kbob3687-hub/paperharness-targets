from pathlib import Path

from mylib import load

rows = load("data.txt", verbose=True)
Path("out.txt").write_text(str(len(rows)), encoding="utf-8")
print("rows", len(rows))
