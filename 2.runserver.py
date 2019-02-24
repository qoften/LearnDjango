'''
这里简单学习了下什么是迁移数据库及尝试运行内置服务器 
    
    创建数据库：
    
我们将修改数据库称之为 迁移数据库
使用迁移命令 migrate
(11_env) PS D:\learning_log> python manage.py migrate
首次执行命令 mugrate 时，Django将数据库与项目当前状态匹配（？）
在使用SQLite（一种使用单个文件的数据库）的新项目首次执行时，Django将新建一个数据库
使用 ls 命令查看，可以发现文件夹多了个文件 db.sqlite3

    
    查看是否创建项目，runserver：
    
pyhon manage.py runserver 启动内置服务器
这里我尝试了使用 PyCharm 的命令行 Terminal 貌似并没有配置，所以报错
（PyCharm-属性-高级-使用管理员运行，成功解决）
使用PowerShell（管理员），cd blog 至目录下再使用python manage.py runserver 成功启动
Django version 2.1.7, using settings 'learning_log.settings'
Starting development server at http://127.0.0.1:8000/

浏览器输入http://localhost:8000/ 或 http://127.0.0.1:8000，页面显示成功！框架运行正常





'''
