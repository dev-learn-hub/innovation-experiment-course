import fitz
import os

pdf_path = r"C:\Users\micha\.openclaw\qqbot\downloads\云南大学课程大纲_1773613221799.pdf"
print(f"正在处理：{pdf_path}")
doc = fitz.open(pdf_path)
print(f"总页数：{len(doc)}\n")
print("="*60)
full_text = ""
for i, page in enumerate(doc):
    page_text = page.get_text()
    full_text += page_text
    print(f"--- 第 {i+1} 页 ---")
    print(page_text)
    print()
