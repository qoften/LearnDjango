'''


此节主要通过为用户添加条目定义模型，使项目与特定主体相关联，这种关系被称为多对一关系
另外再次练习添加新模型，迁移数据库
再通过Django Shell 通过交互式终端会话以编程方式查看输入数据


    （基于app1）添加模型（条目模型, models.py）：
    
class Entry(models.Model):
	'''条目定义模型Entry'''
	'''学到的有关某个主题的具体知识'''
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ForeignKey实例，引用数据库另一条记录，关联特定主题
	text = models.TextField() # TextField文本实例，这里不设置条目长度
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text[:50] + '...'
	'''因为条目文本可能很长，所以设置缩略图只显示前50个字符，后续用省略号点出不是全文'''
  
  
    （添加模型后）迁移、注册模型Entry：
    
由于我们添加了个新模型，需要再次迁移数据库
以后会常用数据迁移,注册，再次回忆一下
>>>>
修改 models.py
>>>>
python manage.py makemigrations app1
>>>>
python manage.py migrate
>>>>
应用目录下注册新模型（admin.py）
from app1.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

【在条目模块Entry增加，迁移，注册完成后 runserver 可以看到网站app1下的Entries目录，可以添加条目了】


    输入一些数据之后，通过交互式终端会话 Django Shell 查看数据：
    
python manage.py shell 启动一个Python解释器，来探索储存在项目中的数据
>>> from app1.models import Topic  # 导入模块app1.models的模型Topic
>>> Topic.objects.all() # 获取模型所有实例
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]> # 返回的列表，称为查询集（queryset）


    像遍历列表一样，遍历查询集，查询每个主题对象ID：
    
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic) # 注意手工缩进4格
...    # <<<<还说怎么没显示每个对象ID，原来是还要再按一次回车
1 Chess
2 Rock Climbing


    知道对象ID后，可以获取对象查看其属性:
    
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2019, 2, 24, 10, 11, 45, 903316, tzinfo=<UTC>)


    查看主题关联条目:
    
>>> t.entry_set.all()
<QuerySet [<Entry: Chess is a two-player strategy board game played o...>]>
 为通过外键关系获取数据，可使用相关模型的 小写名称、下划线和单词set（entry_set）   


每次修改模型后，必须重启shell重载数据，
退出shell >>>> win10使用Ctrl+Z，再回车，其他系统使用Ctr+D






'''
