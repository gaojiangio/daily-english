# 极简更新脚本，只修改index.html的内容，确保能运行
import time

# 读取原有index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 生成新内容（简单的测试文本）
new_news = """
<div class="news-item">1. Practice makes perfect.</div>
<div class="news-item">2. Where there is a will, there is a way.</div>
<div class="news-item">3. A proverb is a short, traditional saying in general use.</div>
"""

# 替换内容 + 更新时间
update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
html_content = html_content.replace(
    "<!-- 自动更新的内容会在这里 -->",
    new_news
).replace(
    "Last update: 2026-02-19",
    f"Last update: {update_time}"
)

# 保存修改
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ 脚本运行成功，index.html已更新！")
