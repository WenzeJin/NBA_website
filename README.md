# NBA Stats and BBS

南京大学网络应用开发课程项目，分为两个部分：

1. NBA 数据查询网站
2. NBA 评论BBS网站

使用的技术栈是：

Django5 + Bootstrap4 + SQLite3 + nba-api

代码编写规范遵循 PEP8

## 运行方法

1. 安装依赖（推荐创建相应虚拟环境，使用`venv`或者`conda`均可）

```shell
$ pip install -r requirements.txt
```
2. 运行数据库迁移

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

3. 运行项目

```shell
$ python manage.py runserver
```

## 开发指南

如果想要参与开发，可以 fork 本项目，然后在本地开发，开发完成后提交 PR。

本项目结构天然地分为两个 Django APP，分别是 `nba` 和 `bbs`，分别对应两个部分的功能。其中，用户的注册和登录功能是共享的，并实现在 `bbs` 中。

请遵循 PEP8 编码规范，参见 [PEP8](https://pep8.org/)。

在提交 PR 前，请确保功能实现正确且没有对原有的功能造成破坏。所有 PR 将经过代码审查后合并。