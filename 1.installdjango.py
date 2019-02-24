
'''
Django的入门学习，首先开始Django的基础安装：

先参考学习腾讯课堂，视频网址：
https://ke.qq.com/course/362788?tdsourcetag=s_pctim_aiomsg
再结合《Python编程 从入门到实践》二次修订

    
    安装指令：（命令行下）

pip install django 在线安装django，本人学习使用版本号为2.1.7

django-admin --version 查看已安装版本号

django-admin 查看更多指令

django-admin startproject <name> 来创造一个web工程(项目)，工程名为<name>，如：django-admin startproject learning_log
django-admin.py startproject <name> . 也可以创建新项目，命令末尾的句点让新项目使用合适的目录结构

    
    Django框架基本目录结构：

1、manage.py 提供了项目的管理命令:
python manage.py.runserver
python manage.py startapp

2、learning_log 项目同名子目录：
__init__.py -包初始化文件
setting.py -网站配置文件
urls -路由配置文件
wsgl.py -wsgl配置文件

'''

