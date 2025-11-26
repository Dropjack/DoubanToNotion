# Douban Notion Book Importer

通过 ISBN 自动从豆瓣获取图书信息，并写入你的 Notion 书目数据库的小工具。

## 功能特点

输入 ISBN → 自动抓取豆瓣图书信息

目前可以自动填充：书名、作者、译者、出版社、出版日期

写入你自己的 Notion 数据库（不会创建额外字段）

自带图形界面，傻瓜式操作


## 如何开始使用？

总共只需要做三件事：

在 Notion 创建 Integration（得到 Token）

把 Integration 加到你的数据库（得到 Database ID）

输入一本书的 ISBN

然后点「导入到 Notion」即可。


### 详细介绍

#### 1️⃣ 获取 Notion Token（Integration Token）





打开：
👉 https://www.notion.so/my-integrations

点击右上角 “+ New integration”

Name 可以填：

BookImporter（或任何你想用的名字）


选择你自己的 Workspace

勾选 “Read content” 和 “Update content” 权限

创建之后，你会看到一个类似这样的 Token：

ntn_123456789abcdeFghijkLMNOPqrsTUV


复制它，粘贴到软件的 “Notion Token” 输入框中。

🔒 Token 就像密码，非常重要。不要给别人。

#### 2️⃣ 获取 Notion Database ID（你的书单页面的 ID）

打开你的 Notion 书单数据库（这个工具会写入这里）

浏览器地址栏里会看到这样的 URL：

https://www.notion.so/1183d1e4250a4e84b7f1bbc7d3ae1b02?v=xxxxxxx


把第一个长串复制出来，就是 Database ID：

1183d1e4250a4e84b7f1bbc7d3ae1b02


粘贴到软件的 “Database ID” 输入框。

#### 3️⃣ 获取 ISBN（从书背面即可）

每本纸质书背面条码上都有 ISBN：

示例：

ISBN 9787532777594


只需要输入数字，不要“ISBN”字样：

9787532777594


粘贴到软件的 “ISBN” 输入框。

---

## 使用方法

打开 NotionBookImporter.exe  

依次填入：

Notion Token

Database ID

ISBN

点击右侧的 “导入到 Notion”



## 数据库字段要求

你的 Notion 表格至少应包含：

书名

出版社

作者

译者

出版日期

字段名称必须与上面一致，否则无法写入对应内容。

工具不会创建新字段，也不会修改其他列。

如果有其他对应修改的需求，请联系我，或自行在python文档中修改
---



## 常见问题
📌 Q1：为什么有些书导不进去？

豆瓣的某些书信息不完整或无数据。
你可以换一个 ISBN 再试，或者手动补充。

📌 Q2：需要一直填 Token 和 ID 吗？

目前需要，但你可以把它们提前填在软件里（自动记住）。
未来版本会加入配置保存。

📌 Q3：可以批量导入一堆 ISBN 吗？

当前版本不支持一次性处理多个 ISBN。
你可以一本一本输入即可（无需重启程序）。

如果你需要批量导入，我们也可以加入此功能。

## License   

MIT License — 可自由使用、修改、分发，无任何限制。
