
'''
Django的入门学习，首先开始Django的基础安装：

结合《Python编程 从入门到实践》二次修订

    
    安装指令：（命令行下）

pip install django 在线安装django（需基于新版python），本人学习使用Django版本号为2.1.7
（注意，书中使用为老版本1.11，新版Django2.0后改动较大，请先明确学习目的，选择合适版本）
如需安装旧版1.11，请使用书中指令pip install Django==1.11

django-admin --version 查看已安装版本号，或使用命令pip show pip

django-admin 查看更多指令

django-admin startproject <name> 来创造一个web工程(项目)，工程名为<name>，
参照书中内容，我们创建个学习笔记的web工程：django-admin startproject learning_log
django-admin.py startproject <name> . 也可以创建新项目，命令末尾的句点让新项目使用合适的目录结构

    
    Django框架基本目录结构：

1、manage.py 提供了项目的管理命令:
python manage.py.runserver
python manage.py startapp

2、learning_log 项目同名子目录(根目录下同名子目录)：
__init__.py # <<<<包初始化文件
setting.py # <<<<网站配置文件
urls.py # <<<<路由配置文件
wsgl.py # <<<<wsgl配置文件

'''

