import numpy as np
from pathlib import Path

# numpy 2 移除了 np.float_，旧论文代码在新版本上会崩
arr = np.array([1.0, 2.0, 3.0], dtype=np.float_)
Path("out.txt").write_text(str(arr.mean()), encoding="utf-8")
print("mean", arr.mean())
