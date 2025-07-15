import nbformat

path = '/sharefs/zhanghp/zhp-private/summer-course-2025/hw3/hw2_notebook.ipynb'

with open(path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb.metadata and "state" not in nb.metadata["widgets"]:
    nb.metadata["widgets"]["state"] = {}

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"{path} finish fixing rendering problem.")