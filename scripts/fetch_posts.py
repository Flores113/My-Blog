import json
import os
import sys
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

if not REPO:
    # 本地运行时的回退，可改为你的 用户名/仓库名
    REPO = "Zhischooler/zemlo"

url = f"https://api.github.com/repos/{REPO}/issues?state=open&per_page=100"
req = urllib.request.Request(url)
if TOKEN:
    req.add_header("Authorization", f"Bearer {TOKEN}")
req.add_header("User-Agent", "zemlo-blog-builder")

try:
    with urllib.request.urlopen(req) as resp:
        raw_posts = json.load(resp)
except Exception as e:
    print(f"获取 Issues 失败: {e}", file=sys.stderr)
    sys.exit(1)

posts = []
for p in raw_posts:
    # 过滤掉 Pull Requests（Issues API 会同时返回 PR）
    if "pull_request" in p:
        continue
    posts.append(
        {
            "number": p["number"],
            "title": p["title"],
            "created_at": p["created_at"],
            "labels": [{"name": l["name"], "color": l.get("color", "")} for l in p["labels"]],
            "body": p.get("body") or "",
        }
    )

# 按创建时间降序（最新在前）
posts.sort(key=lambda x: x["created_at"], reverse=True)

os.makedirs("src/data", exist_ok=True)
with open("src/data/posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"✅ 已生成 src/data/posts.json，共 {len(posts)} 篇文章")
