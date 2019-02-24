'''

Django项目由一系列应用程序组成

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

先明确学习笔记（learning_log）项目的期望功能：
每个用户能在学习笔记中创建主题
输入条目以文本形式显示，且能与特定主题关联
最好记录每个条目的时间戳

打开models.py（本人学习是使用PyCharm打开learning_log文件夹）


















'''
