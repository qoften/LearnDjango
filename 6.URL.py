'''


使用Django创建网页一般分三个阶段：
    定义URL
    编写视图
    编写模版
    
URL模式描述了URL是如何设计，让Django知道如何将浏览器请求与网站URL匹配，以返回对应页面。
每个 URL 第映射至特定 视图 ，视图函数 通常调用一个模版，以生成浏览器可理解的网页。
本节创建学习笔记主页，定义主页URL，编写其视图函数并创建相应模版。


    映射URL：
    
用户通过浏览器输入URL及单击链接来请求网页，所以主页URL最为重要，是用户访问项目的基础URL
之前runserver后，基础URL（http://localhost:8000/）返回默认Django网站，以提示我们正确建立项目
现在要将基础URL映射到“学习笔记”主页

    打开项目主文件夹（learning_log）的urls.py：
（书里显示与实际使用新版不同，后续代码已按新版重新编排）

from django.conf.urls import include, url # 导入了管理URL的函数和模块
from django.contrib import admin

urlpatterns = [
    path(r'admin/', include(admin.site.urls)), # 定义变量 urlpatterns 包含模块admin.site.urls，定义可在管理网站请求中的所有URL
    path(r'', include('app1.urls', namespace='app1')), # 书原文为learning_logs，替换为app1，便于区分（别忘了末尾的,）
]

>>>>书中旧版本见上，新版编写方式见下，在此列出，便于比对适应新旧变化：

# 新版前两行默认缩略，显示为 import... 点开 ... 查看，书显示上两行（1.1.0版本）与新版（2.1.7）下两行作用相符
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), # 定义变量 urlpatterns 包含模块admin.site.urls，定义可在管理网站请求中的所有URL
    path('', 'app1.urls', namespace='app1'), # ''内没有，代表默认的首页，实参 namespace 可将app1的URL与其他分开，便于后续扩展（别忘了末尾的,）
]

    在app1文件夹下添加urls.py（新版2.1.7方法）：
    
（我是PyCharm打开项目，app1文件夹-鼠标右键-New-File-输入urls.py ）

'''定义app1的URL模式''' #首行添加文档字符串，以区分是哪个app的urls.py

from django.urls import url # 导入函数URL，将URL映射到视图

from . import views # 导入模块views，其中的 . 句点让Python从当前urls.py所在文件夹导入视图

urlpatterns =[
    # 主页
    url('^$', views.index, name='index'), # 别忘了后面的,
]

URL模式是一个对函数url（）的调用，函数接受三个实参
>>>>正则表达式（regex）：几乎每个编程语言都会用到，后续也将多次用到
    在这里，Django在urlpatterns中查找与请求URL字符串匹配的正则表达式，即定义了Django可查找的模式
    剖析一下正则表达式（旧版） r'^$' 
    r 让Python将后续字符串视为原始字符串，新版不需添加，或因该设置已改为默认
    '' 圈定正则表达式范围
    ^ 脱字符（^）让Python查看字符串开头
    $ 让Python查看字符末尾
    如果请求的URL与任何URL不匹配，Django将返回一个错误页面
>>>>第二个实参，调用views.index（具体见下）
>>>>第三个实参，将URL模式名称指定为'index'，以方便我们再其他地方引用它，需提供链接时，使用该名称而不用编写URL


    编写模版index.html：
    
模版 定义了网页的结构，指定了网页是什么样子。模版让你能够访问视图提供的任何数据。
app1中新建一个文件夹，命名为templates，该文件夹中再建立一个文件夹logs（建立Django可以明确解读的结构）
在最里面的logs中，新建一个File 命名为index.html，在该文件中写入
<p>Learning Log</p> # 标签<p></p>标识段落，<p>指出开头，</p>标出结尾

<p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>

# 这里定义了两个段落，第一个标题，第二个阐述用途


    编写视图views.py：
    
app1中的 views.py 是由之前 python manage.py startapp 时自动生成
其内置函数 render（） 根据视图提供的数据渲染响应，编入以下行：

def index(reuest):
    '''学习笔记主页'''
    return render(request, 'app1/index.html') # 两个实参，原始请求对象和创建网页模版


再次请求基础URL（http://localhost:8000/admin/），转到刚才创建的网页
Django接受请求的URL，发现该URL与模式''匹配，因此调用函数views.index(),使用index.html包含的模版渲染网页并展示





'''
