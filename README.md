# LearnDjango
本人Django的学习笔记
基于《Python编程 从入门到实践》


目录：

0.env.py 虚拟环境的安装（将项目库与其他项目隔离，方便后期部署到服务器，非必须）

1.installdjango.py 安装Django（本人学习基于Django新版2.1.7，与书中1.11版本稍有变化）

2.runserver.py 学习migrate迁移数据库和runserver运行服务器

3.startapp.py 为项目增加应用，导入模块并激活 

4.superuser.py 简单了解网站分级管理，登录并尝试在网页APP1中添加主题

5.djangoshell.py 以添加一个条目模型为例学习新增模型操作【新增、迁移、注册】，
使用交互式终端对话 Django shell 查看之前输入的条目数据

6.URL.py 学习创建网页三个阶段：定义URL，编写模板，编写视图。
了解正则表达式regex（Django2.0 path写法重编译）

7.baseindex.py 创建包含通用元素的父模版，子模版继承，创建其他页面（显示所有/特定主题页面）
