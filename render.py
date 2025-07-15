import nbformat

path = "/sharefs/zhanghp/zhp-private/summer-course-2025/hw3/hw2_notebook.ipynb"
nb = nbformat.read(open(path, 'r', encoding='utf-8'), as_version=4)

# 删除 metadata 中的 widgets 字段
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# 删除每个 cell 输出中与 widgets 相关的内容
for cell in nb.cells:
    if "outputs" in cell:
        cell["outputs"] = [
            o for o in cell["outputs"] if o.get("output_type") != "display_data" or
            "application/vnd.jupyter.widget-view+json" not in o.get("data", {})
        ]

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("✅ 已删除 widgets 元数据和 cell 中的 widget 输出")
