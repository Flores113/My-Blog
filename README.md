# Zemlo Blog

一个极简、克制的 GitHub Issues 驱动博客模板，基于Gmeek设计。


> [!NOTE]
> 跟你们说，本来是想做的Python+Astro的，结果不知道为什么主要语言成了CSS😂


## 特性

- 📝 使用 GitHub Issues 写作
- 🎨 Gmeek 风格的极简 UI
- 🌙 支持深色/浅色模式切换
- 💬 集成 Utterances 评论系统
- 🚀 自动部署到 GitHub Pages

## 使用方法

1. Fork 或 Use this template 创建你的仓库
2. 修改 `public/config.json` 中的配置
3. 在 Issues 中创建新文章（可添加任意标签）
4. 运行`Deploy Zemlo`这个工作流（Acitons)，接下来等待 GitHub Actions 部署
5. 访问 `https://你的用户名.github.io/你的仓库名/`

## 配置说明

编辑 `public/config.json`：
````json
{
"title": "博客标题",
"description": "博客简介",
"avatar": "头像URL",
"website": "个人网站",
"email": "邮箱地址",
"repo": "用户名/仓库名",
"utterancesRepo": "用户名/仓库名"
}
````


## 评论系统

需要在仓库中安装 [Utterances](https://github.com/apps/utterances)这个 GitHub App。

## License

GPLv3
