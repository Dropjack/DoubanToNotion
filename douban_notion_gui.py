#!/usr/bin/env python3
"""
Tkinter GUI 壳子：输入 Token / Database ID / ISBN，点击按钮导入到 Notion。

核心逻辑全部来自 douban_notion_core.run_import，
这里不再重复那一堆解析/请求代码。
"""

from tkinter import *
from tkinter import scrolledtext, messagebox

from douban_notion_core import run_import


# -------------------- GUI 行为 --------------------


def log(msg: str) -> None:
    log_box.insert(END, msg + "\n")
    log_box.see(END)


def import_to_notion() -> None:
    token = token_entry.get().strip()
    database_id = dbid_entry.get().strip()
    isbn = isbn_entry.get().strip()

    if not token or not database_id or not isbn:
        messagebox.showerror("错误", "请填写 Token、Database ID 和 ISBN")
        return

    log("开始导入…")
    log(f"ISBN: {isbn}")

    try:
        result = run_import(token, database_id, isbn)
    except Exception as e:
        log(f"[ERROR] {e}")
        messagebox.showerror("导入失败", str(e))
        return

    book = result["book"]
    page = result["page"]

    log(f"书名：{book.get('title')}")
    log(f"出版社：{book.get('publisher')}")
    log(f"作者：{', '.join(book.get('author') or [])}")
    log(f"译者：{', '.join(book.get('translator') or [])}")
    log(f"出版日期（原始）：{book.get('pubdate')}")

    url = page.get("url", "<无 URL>")
    log("🎉 成功导入到 Notion！")
    log(f"页面地址：{url}")


def clear_log() -> None:
    log_box.delete(1.0, END)


def exit_program() -> None:
    root.destroy()


# -------------------- Tkinter 布局 --------------------


root = Tk()
root.title("Notion 导入工具（豆瓣 ISBN）")
root.geometry("650x480")

Label(root, text="Notion Token:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
token_entry = Entry(root, width=70)
token_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Database ID:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
dbid_entry = Entry(root, width=70)
dbid_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="ISBN:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
isbn_entry = Entry(root, width=40)
isbn_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

btn_import = Button(root, text="导入到 Notion", command=import_to_notion)
btn_import.grid(row=2, column=2, sticky="w", padx=5, pady=5)

Label(root, text="日志窗口:").grid(row=3, column=0, sticky="nw", padx=10)
log_box = scrolledtext.ScrolledText(root, width=80, height=20)
log_box.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

btn_clear = Button(root, text="清空日志", width=10, command=clear_log)
btn_clear.grid(row=4, column=0, padx=10, pady=10)

btn_exit = Button(root, text="退出", width=10, command=exit_program)
btn_exit.grid(row=4, column=1, sticky="e", padx=10, pady=10)

root.columnconfigure(1, weight=1)   # 让中间那列（所有 Entry）可以自适应宽度
root.columnconfigure(2, weight=0)   # 按钮那列宽度保持固定就好
root.rowconfigure(3, weight=1)      # 日志那一行可以拉伸

root.mainloop()
