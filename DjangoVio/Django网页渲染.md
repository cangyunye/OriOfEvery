# Django网页渲染

## 自定义app风格[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial06/#customize-your-app-s-look-and-feel)

对于我们的`polls`app，首先创建一个目录 `static` 放在 `polls` 目录下。 Django就在这个静态目录查询配置。类似查询template，`polls/templates/`.

Django的[`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATICFILES_FINDERS)包含了一系列，如何查找静态文件的方法。默认的方法是。`AppDirectoriesFinder`在每个 [`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-INSTALLED_APPS)目录指定的APP目录下查找`static`目录。

在 `static`目录里面创建一个 `style.css`. 如`polls/static/polls/style.css`.

## 静态文件的命名空间

为了区分在不同app下有相同名称的静态文件，我们需要为静态文件设置命名空间。简单来说，就是将静态文件放到app下的static目录下，并使用app名称命名。

polls/static/polls/style.css[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial06/#id1)

```css
li a {
    color: green;
}
```

polls/templates/polls/index.html[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial06/#id2)

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

>  `{% static %}` template 标签生成静态文件的URL绝对地址。



## 增加背景图片

**polls/static/polls/images/background.gif**

polls/static/polls/style.css[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial06/#id3)

```css
body {
    background: white url("images/background.gif") no-repeat;
}
```



## 自定义admin form[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial07/#customize-the-admin-form)

将 `Question`模型注册到 `admin.site.register(Question)`, Django就可以构建默认的admin内的表单。

### 变更字段顺序

polls/admin.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial07/#id1)

```python
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

`fields`属性，可以对字段进行直接的调整，如上，直接改变了question_text的字段顺序到pub_date之后



### 为字段定义小标题

```python
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```

>  如果使用`fieldsets`，则可以输出小标签标题



### 添加外键关联对象

对于`Question`,应该有多个`Choice`s，但是admin页并没有展示。

有两种方法可以解决这个问题，**方法1：**

同之前`Question`一样，直接在admin内注册

polls/admin.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial07/#id3)

```python
from django.contrib import admin

from .models import Choice, Question
# ...
admin.site.register(Choice)
```

> - 相当于直接新增了admin页的Choice数据处理
> - 对于Choice页面的Question使用的选择栏方式展示
> - 另外可以点击`add another`按钮，直接打开外键的小窗口进行`Question`数据的添加，这就是Django对外键的处理方式。

**方法2：**

直接修改admin.py的Question

polls/admin.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial07/#id4)

```python
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

> - 'classes': ['collapse'] 表示本段可以隐藏
> - inlines属性选择后面接的内容，这里是外键关联的`Choice`
> - admin.StackedInline表示展示的形式，堆叠式
> - admin.TabularInline则是列表式
> - extra表示额外的式数量



## 自定义admin change list

polls/admin.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial07/#id7)

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 增加一个过滤器的边栏，过滤值依据数据的属性
	list_filter = ['pub_date']
	# 增加搜索器
	search_fields = ['question_text']
```

> [`list_display`](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)可以将注册的APP中的属性字段或者方法在`change`页列做字段展示
>
> `list_filter`增加一个按字段类型的过滤器
>
> `search_fields`增加按字段的搜索器

## 模板重载

从django.contrib.admin.templates.admin复制`*.html`出来到project目录下的templates/admin/目录下，然后重新设置urls.py改变路由指向