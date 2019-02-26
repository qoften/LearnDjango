'''
请在本节起，将上节的logs文件夹替换为app1，代码中所有logs均替换为app1，避免html冲突！！！

  模板继承：

创建网站时，几乎都有些共用的网站元素，在这类情况下，编写一个包含通用元素的父模板（base.html），再通过子模板(index.html)继承
便于让你专注开发每个网页的独特方面，同时让整个项目结构更加清晰简洁
使得网站修改更新更立体快捷，大型项目中，通常有一个全网站的父模板base.html，
每个网站主要部分也会有个父模板，每个部分的父模板继承base.html，各网页再继承相应部分的父模板
（Python 代码通常缩进 4 个空格，模板 缩进层数更多，因此通常只缩进 2 个空格）


  父模板:

在之前的 index.html 目录中，创建一个名为 base.html 的父模板，包含所有公用元素。
当前公用部分只包含顶端标题，因此我们这么设置
<p>
    <a href="{% url 'app1:index' %}">Learning Log</a> # 创建段落，使用模板标签创建链接，段落包含项目名
</p>

{% block content %}{% endblock content %} # 一对块标签，名为content，作为占位符，信息由子模块指定

模版标签 用｛% %｝表示，{% url 'app1:index' %} 中，生成一个url与app1中views.py指向的urls.py定义URL模式匹配
在这里 logs 是一个命名空间，index是该命名空间名称独特的URL模式

在简单HTML页面中，链接使用 锚标签 定义：<a href="link_url">link text</a>
让模板标签生成URL，修改项目URL，只需修改urls.py的URL模式，以后网页被请求时，Django会自动插入修改后的URL


  子模板：
    
重新编写 index.html，使其继承 base.html：
｛% extends "app1/base.html" %｝ # 原标题替换从父模板继承的代码，让Django知道继承了哪个父模板

{% block content %} # 定义content 不是从父模板继承的内容都包含在content块中

<p>
    Learning Log helps you keep track of your learning, for any topic you're learning about.
</p>

# 这里定义了两个段落，第一个标题，第二个阐述用途

{% endblock content %} # 定义结束位置


  高效网页创建——显示全部主题的页面：
  
新建、模块、视图三步走




'''
