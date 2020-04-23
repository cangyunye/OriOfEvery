# Django测试

## TestCase类测试

在对应app下目录创建test*.py文件

polls/tests.py[¶](https://docs.djangoproject.com/en/3.0/intro/tutorial05/#id1)

> 判断最近发布日期如果超过当前时间则返回False

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```



运行命令

`python mange.py test polls`

`test*.py`文件会被自动找出来然后执行。

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

> 1. 这里使用到Django自带的模块django.test.TestCase。
> 2. 测试过程会自动创建测试用的数据库
> 3. 自动找寻名称以`test`开头的方法，如test_was_published_recently_with_future_question

## 用shell测试

我们通过 [`shell`](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-shell)启动首先在 [`shell`](https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-shell)中配置环境:

```python
$ python manage.py shell
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

[`setup_test_environment()`](https://docs.djangoproject.com/en/3.0/topics/testing/advanced/#django.test.utils.setup_test_environment) 安装了template进行渲染，允许我们检查responses中的某些属性，比如 `response.context` 要注意的是这个方法**并没有安装测试数据库**，而是直接使用存在的数据库，也就是说，输出有可能依赖于已经创建的数据。在此之前，注意 `TIME_ZONE` 在 `settings.py`  设置，以便数据时间不会出错。

首先是导入`Client`类

```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

后续操作

```python
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```