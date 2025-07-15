import nbformat

path = '/sharefs/zhanghp/zhp-private/summer-course-2025/hw3/hw2_notebook.ipynb'

with open(path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" not in nb.metadata:
    nb.metadata["widgets"] = {}

nb.metadata["widgets"].setdefault("state", {})
nb.metadata["widgets"].setdefault("version", "1.0.0")

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"{path} finishing fixing rendering problem.")