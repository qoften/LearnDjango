'''


为了管理网站，我们必须将权限分级，并使用超级用户管理

    创建超级用户superuser：
    
python manage.py createsuperuser 创建超级用户帐号：    
(11_env) D:\learning_log>python manage.py createsuperuser
Username (leave blank to use 'qofte'): admin
Email address: superuser@gmail.com
Password:
Password (again):
Superuser created successfully.

这里用户名，邮箱，密码自行设置，帐号默认为PC用户名，密码输入时光标不移动
当密码为全数字时会提示 This password is entirely numeric. 提示你密码不能全为数字


    向管理网站注册模型：
    
Django自动在管理网站中添加模型，如User和Group，但对于我们创建的模型，需要手工注册
在app1目录下，我们找到admin.py，输入以下代码
from app1.models import Topic
admin.site.register(Topic)

我是在PyCharm下编辑后直接左下角 Terminal 调出命令行
python manage.py runserver 运行（或者其他方式激活虚拟环境），看到登录界面，
使用超级用户帐号密码登录，成功！
该网页可以让你进行多种操作，比如
编辑已加载应用APP的主题，添加和修改用户和用户组等


    添加主题：
    
点击应用APP1标题Topics的Add，添加一个主题
输入主题名称，并save（我按教程添加的 Chess 和 Rock Climbing）


'''
