'''

Django项目（Web工程）一般是由一系列应用程序组成

在runserver后
我们得到的是一个空白的页面，现在我们尝试在其中增加 startapp 一些应用（学习笔记learning_log项目）：


    创建一个应用程序：
    
在之前PowerShell虚拟环境env下保持runserver运行，
另开一个终端窗口如PowerShell（或新标签页），开虚拟环境，切换到manage.py目录下
d:
cd learning_log
11_env\Scripts\activate
执行命令 startapp 新增文件夹<app1> 
python manage.py startapp app1
使用 ls 和 ls app1/ 查看目录内文件变化
其中增加的文件包含
models.py 定义要在应用程序管理的数据
admin.py 作用待补充
views.py 作用待补充
__init__.py -包初始化文件

如上线该app需将app添加至 settings 的 installed-apps 列表


    明确学习笔记项目（learning_log）目标：
    
每个用户能在学习笔记中创建主题
输入条目以文本形式显示，且能与特定主题关联
最好记录每个条目的时间戳


    创建模型：
    
打开models.py（本人学习是使用PyCharm打开learning_log文件夹）

models.py

from django.db import models

# Create your models here.

class Topic(models.Model):
	'''用户学习的主题'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text


    激活模型：
    
打开setting.py，在INSTALLED_APPS里添加app1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1', # 添加应用程序app1
]

python manage.py makemigrations app1 使用 makemigrations 命令来让Django替我们修改数据库，储存相关联的数据

python manage.py migrate 应用迁移

当需要修改数据时，一般都采取以上三个步骤：

（所需修改的APP）修改models.py
对项目调用makemigrations
使用命令 migrate 让Django迁移项目









'''
