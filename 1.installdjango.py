
'''
今日开始Django的入门学习，首先开始Django的基础安装：
先参考学习腾讯课堂，视频网址：
https://ke.qq.com/course/362788?tdsourcetag=s_pctim_aiomsg

    安装指令：（命令行下）

pip install django 在线安装django，本人学习使用版本号为2.1.7

django-admin --version 查看已安装版本号

django-admin 查看更多指令

django-admin startproject <name> 来创造一个web工程，工程名为<name>，如：django-admin startproject myblog

    Django框架基本目录结构：

1、manage.py:
提供了项目的管理命令
python manage.py.runserver
python manage.py startapp

2、myblog同名子目录：
__init__.py -包初始化文件
setting.py -网站配置文件
urls -路由配置文件
wsgl.py -wsgl配置文件

    创建网站的具体应用：
1、创建一个模块
python manage.py startapp articles 创建一个app

2、执行后目录会生成一个 articles 的目录(目录参考myblog)
__init__.py -包初始化文件
setting.py -网站配置文件
urls -路由配置文件
wsgl.py -wsgl配置文件

3、将app添加至 settings 的 installed-apps 列表

'''

