# 静态网页加载

1. 想建个导航页，命名app为`navi`，`python manage.py startapp navi`
2. 将写好的index.html静态页模板放到app目录下`navi/templates/navi/index.html`
3. `cd navi`，编辑views.py 添加一个函数

```python
def hi(request):
	return render(request,"navi/index.html")
```

3. 修改工程下的settings
   - 增加TEMPALTES下的DIRS对应本目录，如果不增加的话，可以直接放到项目templates目录下或者app的templates目录下
   - 增加INSTALLED_APPS `navi`，确保`django.contrib.staticfiles`也在，用于后续加载模板的css样式

```python
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'navi'
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'navi')],
```

4. urls.py增加路由`urlpatterns`

   - 先从工程级urls.py设置

     ```python
     urlpatterns = [
         ...
         path('hi/', nv.hi),
     ]
     ```
     
    - 再app级urls.py设置，来关联到之前的view
   
      ```python
      urlpatterns = [
          ...
          path('',views.hi,name='hi'),
      ]
      ```
   
5. css加载，在index.html里面增加如下内容，表示从`navi/static/`下的目录追踪一下css或js

   ```html
   {% load static %}
   <link rel="stylesheet" type="text/css" href="{% static 'navi/bootstrap/dist/css/bootstrap.min.css' %}">
     <script src="{% static 'navi/jquery/dist/jquery.min.js' %}"></script>
     <script src="{% static 'navi/popper.js/dist/popper.min.js' %}"></script>
     <script src="{% static 'navi/bootstrap/dist/js/bootstrap.min.js' %}"></script>
   
   
   ```

   

# 静态文件引用
   最后，在index.html中引入外部资源文件时，使用如下方式进行引用：

   js文件：`<script src="/static/js/jquery.js"></script>`
   css文件：`<link href="/static/css/bootstrap.min.css" rel="stylesheet">`
   图片：`<img class="img-responsive" src="/static/img/phones.png" alt="">`
   或者进行如下引用：

   先在index.html文件中输入：`{% load staticfiles %}`，再按如下方式进行引用。

   js文件：`<script src="{% static 'js/jquery.js' %}"></script>`
   css文件：`<link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">`
   图片：`<img class="img-responsive" src="{% static 'img/phones.png' %}" alt="">`
   ————————————————

# \<iframe\>元素嵌入网页访问

对views.py中需要访问的网页加载装饰器，去掉iframe限制

```python
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def msgb(request):
	if request.method == 'GET':
		msg = msgboard.objects.all()
		context = {"messages":msg}
		return render(request,"navi/messageboard.html",context=context)

```






# 协同forms使用

## HTML forms

在html中 通过标签`<form>...<form>`可以让游客输入文本，选项选择，操作对象和其他控制，然后发送信息到服务器

这些表单接口元素，**文本输入**或者**检查框** 是HTML**内置元素**，其他复杂元素，如一个接口弹出日期选择器或者华东滑条来操控是典型的JavaScript和Css以及HTML`<input>`标签的典型应用

对于`<input>`元素来说，一个表单必须指定2个东西：

- where: 对于处理用户输入的数据需要返回的URL地址
- how: 通过何种HTTP方法返回

举个例子，登录Django admin包含一些`<input>`元素，`type="text"`对username,`type="password"`对password，`type="submit"`对log in 按钮。它也包含了一些隐藏的文本控件，用户看不见，而Django用来决定后续操作的。

`<form>`的`action`属性来告诉浏览器，这个表单数据将会发送到的URL，比如指向`/admin/`地址，然后通过`method=POST`发送。

**<input type="submit" value="Log in">** 按钮触发时，数据就返回`/admin/`



## GET  AND POST

这两种方法是HTTP方法用于处理表单(form)的。

**POST**方法是用来绑定表单数据，编码然后传递到服务器然后接受服务器返回。

**GET**方法是提交一组数据绑定到字符串，组成URL，URL包含数据将要发送的地址，以及数据key和value。

如`https://docs.djangoproject.com/search/?q=forms&release=1`











