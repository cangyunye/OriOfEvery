# 基本配置



## [urls.py](https://code.ziqiangxuetang.com/django/django-views-urls.html)

网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。

相当于路由器，但是route可以不加`.html`作为尾缀，那就需要加入`/`，**不推荐前者**

`path(route, view, kwargs=None, name=None, Pattern=None)`

> 根据用户输入的网址，先从根级urls.py匹配到app级urls.py的path的route，然后从views的HttpResponse获取返回内容



## [views.py](https://code.ziqiangxuetang.com/django/django-views-urls.html)

处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，**用户请求的数据，输出到网页。**

也就是在这里将实际进行的数据处理进行反馈到用户，比如从数据库提取数据，或者进行数据计算

返回的对象是`HttpResponse`或者`exception`

## [models.py](https://code.ziqiangxuetang.com/django/django-models.html)

与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。

models定义的数据类型都继承自`models.Model`

所有数据类型都有Manager对象，比如Person模型，如果不在模型内重新定义models.Manager()，则Person.objects即代表Manager对象

```python
from django.db import models

class Person(models.Model):
    #...
    people = models.Manager()

```

如果使用了这个模型， Person.objects会产生AttributeError exception，而Person.people.all() 就可以正确提供Person的所有对象。

## forms.py

## [forms.py](https://code.ziqiangxuetang.com/django/django-forms.html)

表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作，当然你也可以不使用。

**templates 文件夹**

views.py 中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度。

## [admin.py](https://code.ziqiangxuetang.com/django/django-admin.html)

后台，可以用很少量的代码就拥有一个强大的后台。

## [settings.py](https://code.ziqiangxuetang.com/django/django-settings.html) 

Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。

## 时区

```
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True
```

如果`USE_TZ`使用时区开关打开，那么数据库的所有时间都是按照UTC来，而不是按照服务器时间来，所以通常来说这里可以关闭。

# manage.py

到项目目录下，带有manage.py的目录

## 创建project

`python manage.py startproject Vio #创建Vio工程`


```bash
Vio
├── manage.py
└── Vio
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 创建app

`python manage.py startapp learn`

```
learn
├── __init__.py
├── admin.py    后台相关的设置
├── apps.py     app相关的设置文件
├── migrations  数据库变更相关
│   └── __init__.py
├── models.py   数据库模型相关
├── tests.py    单元测试
└── views.py    视图逻辑
```


### 定义url和app

新定义的app加到`settings.py`中的**INSTALL_APPS**中

```python
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learn',   # 注意添加了这一行
]
```
`urls.py`

```python
from django.contrib import admin
from django.urls import path
from learn import views as learn_views  # new
 
urlpatterns = [
    path("", learn_views.index),  # new
    path('admin/', admin.site.urls),
]
```
## 启动server

`python manage.py runserver 0.0.0.0:8000` 

1. 这里使用0.0.0.0指使用本机的所有IP地址

从127.0.0.1:8000端口进入

```bash
(venv) F:\DreamToDream\OnMyWay\Programming\Python\DjangoVio\Vio>python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 28, 2020 - 11:37:23
Django version 3.0.2, using settings 'Vio.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
[28/Jan/2020 11:37:27] "GET / HTTP/1.1" 200 16351
[28/Jan/2020 11:37:27] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
Not Found: /favicon.ico
[28/Jan/2020 11:37:27] "GET /favicon.ico HTTP/1.1" 404 1969
```



1. http://127.0.0.1:8000/admin 管理员登录
2. http://127.0.0.1:8000 首页（在定义了url和app后，就会从urls.py跳转到views）

# urls.py

1. 采用`/add/?a=4&b=5 `这样的方法进行get

`python manage.py startapp calc`

在**calc/views.py**中定义

```python
from django.shortcuts import render
from django.http import HttpResponse
 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
```

> request.GET是一个字典，因此，可以使用request.GET.get('a',0)防止某些意外

## 根级urls.py

然后再修改根级的**urls.py**，添加一个网址`add`来对应我们刚刚的视图

```python
path('add/',calc_views.add,name='add'), #务必在add后面加"/"```


2. 采用/add/4/5这样的方式

在**calc/views.py**定义add2

​```python
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
```

```python
path('add/<int:a>/<int:b>/',calc_views.add2,name='add2'), # add_new
```

> 1. path的变量定义和views.py中的a,b变量什么关系
>
>    --在path中，`<int:a>`中的前者表示值类型，冒号后的为视图view.add2的入参a
>
> 2. path中的name参数是什么东西
>
> 3. settings.py中的INSTALLED_APPS有什么用


### include()

在根级**urls.py**，urlpatterns的path对象的views参数可以通过include来指定关联app级url地址，类似python的包导入

如include('polls.url')，相当于导入polls包(包需要带有`__init__.py`)下的url.py



## 应用级urls.py

在app新建urls.py，

```python
from django.urls import path

from . import views

urlpatterns = [
	path('ref/',views.index,name='index'),
]
```

在这里的path中的`ref/`可以相对于根级(项目级)urls.py增加相对路径

# settings.py

## 数据库设置

默认情况下使用sqlite3

[`DATABASES`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DATABASES)

- ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are also available.
- NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.

[`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-INSTALLED_APPS) 

- [`django.contrib.admin`](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#module-django.contrib.admin) – The admin site. You’ll use it shortly.
- [`django.contrib.auth`](https://docs.djangoproject.com/en/3.0/topics/auth/#module-django.contrib.auth) – An authentication system.
- [`django.contrib.contenttypes`](https://docs.djangoproject.com/en/3.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes) – A framework for content types.
- [`django.contrib.sessions`](https://docs.djangoproject.com/en/3.0/topics/http/sessions/#module-django.contrib.sessions) – A session framework.
- [`django.contrib.messages`](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#module-django.contrib.messages) – A messaging framework.
- [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles) – A framework for managing static files.

在使用以上默认应用之前，需要先创建数据库

`python manage.py migrate`

以上命令可以创建或者同步数据库在`models.py`中的配置概要，并且无需删除原有数据库而是直接实时更新（通常来说，除非有大的变动）



# models.py

> 这个东西看起来向定义数据结构
>
> 1. 每个类为一个表，或者说一个数据模型
> 2. 而\*Field的对象则是字段类型，而赋值的变量名称即列字段



# apps.py

Django中的App可以部署到多个项目

app需要在`project/settings.py`设置

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



## 通过models生成migrations文件

启动命令:`python manage.py makemigrations polls`

会将`models.py`中配置的模型生成migrations数据类

## 创建sql生成语句

启动命令:`python manage.py sqlmigrate polls 0001`

```sql
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```



> - 生成的语句是根据使用的数据库引擎来的。上面是使用的默认引擎，sqlite3
> - 表名称是组合`app`名称和下划线`_`和类名`Class`
> - 主键ID是自动补充的，不过可以自行覆盖
> - 依据惯例，外键会增加下划线`_id`。也可以自行覆盖
> - 外键直接通过 `FOREIGN KEY` 约束说明。无需担心 `DEFERRABLE` 这个部分; 它表明sqlite3在事物结束之前不会强制使用外键
> - It’s tailored to the database you’re using, so database-specific field types such as `auto_increment` (MySQL), `serial` (PostgreSQL), or `integer primary key autoincrement` (SQLite) are handled for you automatically. Same goes for the quoting of field names – e.g., using double quotes or single quotes.
> - 命令 [`sqlmigrate`](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-sqlmigrate) 不是直接在数据库上迁移，而是只将Django所分析的语句打印在屏幕上. 

## 检查

`python manage.py check`语句可用于在没有创建数据库的时候进行检查



# 数据模型创建步骤

- Change your models (in `models.py`).
- Run [`python manage.py makemigrations`](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-makemigrations) to create migrations for those changes
- Run [`python manage.py migrate`](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-migrate) to apply those changes to the database.



# API接口

## Django shell

启动命令：`python manage.py shell [-i ipython/bpython]`

We’re using this instead of simply typing “python”, because `manage.py` sets the `DJANGO_SETTINGS_MODULE` environment variable, which gives Django the Python import path to your `mysite/settings.py` file.

Once you’re in the shell, explore the [database API](https://docs.djangoproject.com/en/3.0/topics/db/queries/):

```
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Wait a minute. `` isn’t a helpful representation of this object. Let’s fix that by editing the `Question` model (in the `polls/models.py` file) and adding a [`__str__()`](https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.__str__) method to both `Question` and `Choice`:

polls/models.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#id4)

```
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

It’s important to add [`__str__()`](https://docs.djangoproject.com/en/3.0/ref/models/instances/#django.db.models.Model.__str__) methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.

Let’s also add a custom method to this model:

polls/models.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#id5)

```
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Note the addition of `import datetime` and `from django.utils import timezone`, to reference Python’s standard [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime) module and Django’s time-zone-related utilities in [`django.utils.timezone`](https://docs.djangoproject.com/en/3.0/ref/utils/#module-django.utils.timezone), respectively. If you aren’t familiar with time zone handling in Python, you can learn more in the [time zone support docs](https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/).

Save these changes and start a new Python interactive shell by running `python manage.py shell` again:

```
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

For more information on model relations, see [Accessing related objects](https://docs.djangoproject.com/en/3.0/ref/models/relations/). For more on how to use double underscores to perform field lookups via the API, see [Field lookups](https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups-intro). For full details on the database API, see our [Database API reference](https://docs.djangoproject.com/en/3.0/topics/db/queries/).

# Django Admin

1. 创建一个超级管理员

`python manage.py createsuperuser`

Username (leave blank to use 'administrator'): Scarlet
Email address: cangyunye@sina.com
Password:8+
Password (again):
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.



http://127.0.0.1:8000/admin/


## 将app载入admin[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin)

polls/admin.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#id6)

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```



# Django Templates

[Templates](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

settings.py 中的TEMPLATES.APP_DIRS=True表示会从[`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-INSTALLED_APPS)的目录寻找templates文件夹中的模板

> Django会匹配第一个名称对应的模板，因此无法区分相同名称不同目录下的模板。我们需要将对应app的模板放到对应app的templates目录下，使用与app相同的命名方式。

## 变量查询

> **变量查询顺序**：如 `{{ question.question_text }}`Django先从**字典**对象中查找 `question`. 如若无果再从**属性**查找 – 再无果，则从**列表索引**查找

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id5)

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

模板中的`latest_question_list` 是变量在render中作为入参

## 模板加载

polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id6)

通过`django.template.loader`读取模板

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

template.render组装(字典型变量，请求)返回到`HttpResponse`

### 简写render

polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id7)

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

> 简写render(request,模板,替换变量字典)

## 循环语法

polls/templates/polls/detail.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id11)
> for循环： [`{% for %}`](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#std:templatetag-for) `{% endfor %}`

```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```



## 硬编码移除

比如我们写入`polls/index.html`模板的连接为以下方式的硬编码连接:

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

在项目的URLs地址要变换时由于耦合性太强，会要花费大量时间修改。因此可以通过 [`path()`](https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.path) 函数，在`polls.urls` 模块设计通过`name`关联，比如在模板中使用 `{% url %}` 标签:

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

如上的`detail`即在`polls.urls`通过`path`指定的`name`。

```python
...
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
...
```

当想要将地址变成如`polls/specifics/12/`这种时，直接更改`polls/urls.py`即可:

```python
...
# added the word 'specifics'
path('specifics/<int:question_id>/', views.detail, name='detail'),
...
```

## URL命名空间

由于每个app有自己的urls.py，因此，可能就会有同一个blog项目中，存在多个app的urls.py定义了相同path中的name，而模板里面`{% url %}`指定的命名空间就很难区分了，这时候可以在app级的urls.py中设置`app_name`作为命名空间。

polls/urls.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id12)

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Now change your `polls/index.html` template from:

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id13)

```HTML
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

to point at the namespaced detail view:

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id14)

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

> HTML标签里面写模板语法用的是`{{}}`，而标签外使用语法`{}`

# exception

## Http404

针对不存在的数据返回404异常

polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id8)

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

## 简写get_object_or_404

polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial03/#id10)

```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```



# 小型表单form

polls/templates/polls/detail.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial04/#id1)

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

> `<form>`元素即表单，在模板中，`form`标签外加参数`action`和`method="post"`(post为提交到服务端的数据，而`get`为获取服务端的数据)
>
> `<input>`元素是输入框，`type="radio"`，这种形式就是个小圆圈的点选:white_circle:,`name=choice`表示，`POST`发送数据到表单，数据内容为`choice#`，`#`为选项的ID
>
> `forloop.counter`表示`for`标签(`label`)的循环的次数值，也可以说是上层`for`循环到第几次了，如1,2
>
>  [`{% csrf_token %}`](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#std:templatetag-csrf_token) template tag.跨站点请求伪造（Cross-site request forgery）保护。



polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial04/#id3)

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

- [`request.POST`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.POST)是一个类字典对象，允许你在提交的数据中通过字典的key获取，如`request.POST['choice']` 返回选中的choice的ID，string类型（默认）。

  [`request.GET`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.GET) 也是同样作为获取数据的方法，但这里使用 [`request.POST`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.POST) 是为了保证，用户的数据是通过POST方式提交。

- `request.POST['choice']` 会拉起一个 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 如果 `choice` 没在POST数据里面找到。上述代码检查 [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError) 并且展示问题表单作为错误信息。

- choice的votes数增加后返回 [`HttpResponseRedirect`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponseRedirect)而非 [`HttpResponse`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponse). [`HttpResponseRedirect`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponseRedirect) 有一个参数让用户重定向URL。

  就像Python中注释说明一样，使用 [`HttpResponseRedirect`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponseRedirect) 来确保用户操作成功后，处理服务端POST数据后不会二次触发。

-  [`reverse()`](https://docs.djangoproject.com/en/3.0/ref/urlresolvers/#django.urls.reverse) 在 [`HttpResponseRedirect`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponseRedirect) 构造器中作为一个例子，用于避免在VIEW中进行硬编码，直接返回字符串

  如：`'/polls/3/results/'`，中间的3即polls.view中的results的参数question_id



# 通用视图generic views

[generic views documentation](https://docs.djangoproject.com/en/3.0/topics/class-based-views/)

polls/views.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial04/#id7)

```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

> 这里用到了`generic`的`ListView`和`DetailView`，使用哪个View模板取决于你想要展现的形式。
>
> 类中继承的属性如`template_name`如果不自定义的话，对于`DetailView`默认是` <app name>/<model name>_detail.html`
>
> 属性`context_object_name`自动将DetailView中的get_queryset的值组装成字典

polls/urls.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial04/#id6)

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



# 虚拟环境

```bash
pip install virtualenv 
python3 -m venv  --no-site-packages  DjangoVio #创建虚拟环境工程目录
cd DjangoVio\bin
activate # 切换环境变量
deactivate # 恢复环境变量
pip list #查看包
pip freeze > requirements.txt  #导出已安装包
pip install -r requirements.txt #根据文件安装包
```




# 安装问题

win10系统

however the ssl module in Python is not available

https://slproweb.com/products/Win32OpenSSL.html

# 启动问题

```shell
  File "F:\ProgramData\Anaconda3\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "F:\DreamToDream\OnMyWay\Programming\Python\DjangoVio\Vio\venv\Lib\site-packages\django\db\backends\sqlite3\base.py", line 14, in <module>
    from sqlite3 import dbapi2 as Database
  File "F:\ProgramData\Anaconda3\lib\sqlite3\__init__.py", line 23, in <module>
    from sqlite3.dbapi2 import *
  File "F:\ProgramData\Anaconda3\lib\sqlite3\dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ImportError: DLL load failed: 找不到指定的模块。
```

方法1：从这里下载

https://www.sqlite.org/download.html

将解压的sqlite3.def和sqlite3.dll放到 F:\ProgramData\Anaconda3\DLLs

方法2：不使用django-admin.py，而是使用django-admin.exe
具体操作如下 django-admin.exe startapp learn，没有提示错误。



django.core.exceptions.ImproperlyConfigured:



# 连接问题

## 问题1：连接无反应
使用启动方式
`python manage.py runserver 0.0.0.0:8000`
主要是指定`0.0.0.0`，全入口监听

## 问题2：DisallowedHost at /

```
Invalid HTTP_HOST header
```

修改project的
setting.py 文件：

`ALLOWED_HOSTS = ['*']`  ＃在这里请求的host添加了＊

# 学习文档

https://www.djangoproject.com/start/

https://code.ziqiangxuetang.com/django

https://www.w3cschool.cn/django

