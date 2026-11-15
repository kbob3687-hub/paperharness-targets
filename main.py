import yaml
from pathlib import Path

data = yaml.safe_load("name: paperharness\nversion: 1")
Path("out.txt").write_text(f"{data['name']}={data['version']}", encoding="utf-8")
print("parsed", data)
