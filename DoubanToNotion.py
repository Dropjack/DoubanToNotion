#!/usr/bin/env python3
"""
命令行壳子：用 ISBN 从豆瓣导入到 Notion。

用法：
    py DoubanToNotion.py 9787208050037
"""

import os
import sys
from typing import Dict, Any

from douban_notion_core import run_import, REQUIRED_PROPERTIES


# ======= 这里配置你的 Token 和 Database ID =======

# 推荐：在环境变量里设置 NOTION_TOKEN / NOTION_DATABASE_ID
# 但你如果偷懒，也可以直接把默认值改成你自己的。
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")


# ======= 一点小工具 =======


def panic(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)
    sys.exit(1)


def get_isbn_from_argv() -> str:
    """
    从命令行参数里拿 ISBN。
    """
    if len(sys.argv) != 2:
        print("用法：py DoubanToNotion.py <ISBN>")
        sys.exit(1)
    isbn = sys.argv[1].strip()
    if not isbn:
        panic("ISBN 为空。")
    return isbn


# ======= 主流程 =======


def main() -> None:
    isbn = get_isbn_from_argv()
    print(f"[INFO] ISBN: {isbn}")

    if not NOTION_TOKEN or NOTION_TOKEN.startswith("ntn_XXXX"):
        panic("请先在 DoubanToNotion.py 里配置 NOTION_TOKEN。")
    if not NOTION_DATABASE_ID:
        panic("请先在 DoubanToNotion.py 里配置 NOTION_DATABASE_ID。")

    try:
        result: Dict[str, Any] = run_import(NOTION_TOKEN, NOTION_DATABASE_ID, isbn)
    except Exception as e:
        panic(f"导入失败：{e}")

    book = result["book"]
    properties = result["properties"]
    page = result["page"]

    print(f"[INFO] 豆瓣返回的标题：{book.get('title')}")
    print("[INFO] 即将写入 Notion 的字段：")
    for key in REQUIRED_PROPERTIES:
        print(f"  - {key}: {properties[key]}")

    url = page.get("url", "<无 URL>")
    print("[OK] 已成功创建一条记录。")
    print("     Notion 页面地址：", url)


if __name__ == "__main__":
    main()
