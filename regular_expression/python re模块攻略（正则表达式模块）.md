# python re模块攻略（正则表达式模块）

## 常用匹配规则

| 模式     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| `\w`     | 匹配字母、数字及下划线                                       |
| `\W`     | 匹配不是字母、数字及下划线的字符                             |
| `\s`     | 匹配任意空白字符，等价于`[\t\n\r\f]`                         |
| `\S`     | 匹配任意非空字符                                             |
| `\d`     | 匹配任意数字，等价于`[0-9]`                                  |
| `\D`     | 匹配任意非数字的字符                                         |
| `\A`     | 匹配字符串开头                                               |
| `\Z`     | 匹配字符串结尾，如果存在换行，只匹配到换行前的结束字符串     |
| `\z`     | 匹配字符串结尾，如果存在换行，同时还会匹配换行符             |
| `\G`     | 匹配最后匹配完成的位置                                       |
| `\n`     | 匹配一个换行符                                               |
| `\t`     | 匹配一个制表符                                               |
| `^`      | 匹配一行字符串的开头                                         |
| `$`      | 匹配一行字符串的结尾                                         |
| `.`      | 匹配任意字符，除了换行符，当`re.DOTALL`标记被指定时，则可以匹配包括换行符的任意字符 |
| `[...]`  | 用来表示一组字符，单独列出，比如`[amk]`匹配`a`、`m`或`k`     |
| `[^...]` | 不在`[]`中的字符，比如`[^abc]`匹配除了`a`、`b`、`c`之外的字符 |
| `*`      | 匹配0个或多个表达式                                          |
| `+`      | 匹配1个或多个表达式                                          |
| `?`      | 匹配0个或1个前面的正则表达式定义的片段，非贪婪方式           |
| `{n}`    | 精确匹配`n`个前面的表达式                                    |
| `{n, m}` | 匹配`n`到`m`次由前面正则表达式定义的片段，贪婪方式           |
| `a|b`    | 匹配`a`或`b`                                                 |
| `( )`    | 匹配括号内的表达式，也表示一个组                             |

## match()

从字符串的起始位置开始匹配，返回SRE_MATCH对象

```python
import re
#文本内容
content = 'WOW! Stunning sunrise seen this morning from Belle Plaine, Minnesota'
#文本长度
print(len(content))
#匹配特征
pattern = '^\w{3}!\sStunning sunrise\s\w{4}'
result = re.match(pattern,content)
print(result)
#匹配内容
print(result.group())
#匹配范围
print(result.span())
```

> ```python
> #输出结果
> 68
> <_sre.SRE_Match object; span=(0, 26), match='WOW! Stunning sunrise seen'>
> WOW! Stunning sunrise seen
> (0, 26)
> ```

- "**^**"为匹配字符串的开头（对于match方法来说，可以不加，因为是必须从开始位置匹配）

- "**\w**{3}"表示匹配字母、数字、下划线共3位。

- "\s"表示匹配空格。

- 设定的**pattern**中，仅匹配sunrise后+空格(\s)+4个字母(\w)。

- group()方法，返回了匹配的结果。

- span()方法返回了匹配的范围。


### 提取匹配字段

如上文中，想提取**sunrise**和**seen**，可以通过将想提取的子字符串用"()"括起来

```python
pattern = '^\w{3}!\sStunning (sunrise)\s(\w{4})\s\w{4}\s\w{7}'
```

然后通过**group()**方法调用分组索引

```python
>>> print(result.group(1))
sunrise
>>> print(result.group(2))
seen
```

> Tips小技巧:为了简化print某些对索引的输出，我们可以使用匿名表达式
>
> f=lambda x:print(result.group(x))
>
> f(1)会是什么结果呢？

### 通用匹配

在**pattern**中，我们对于"\s"空格和"\w{n}"的多次切换使用，大多时候其实是冗余操作，因此，需要用到".*"进行任意字符匹配

这里从头开始匹配结尾到Minnesota
```python
pattern = '^\w{3}!\sStunning (sunrise).*Plaine$'
```

>```python
>#输出结果
>f=lambda x:print(result.group(x))
>f(1)
>sunrise
>f(2)
>morning
>```

- "."可以匹配任意字符（除换行符），指定re.DOTALL标记可以匹配包括换行符在内任意字符
- "*"可以匹配前面的字符无限次数，与"."组合即无限匹配

### 贪婪与非贪婪

什么是贪婪，这里另外举例子，如果我们想匹配数字，可能，开始想这样设计匹配特征

```python
content = 'Hello 1234567 World'
pattern = '^He.*(\d+).*ld'
```

> print(result.group(0))
>
> Hello 1234567 World
>
> print(result.group(1))
>
> 7

发现结果只有匹配到7，这是因为".*"优先匹配了最多的字符，然后才轮到(\d+)

所以此时可以转换为非贪婪匹配，在".*"后多增加个"?"

```python
pattern = '^He.*?(\d+).*ld'
```

使用非贪婪匹配的时候，必须注意，在结尾使用".*?"，意味着，尽可能少会少到不匹配。

### 修饰符

在正则表达式使用时，常常会遇到一些问题。比如，字符串换行时，发现无法匹配了

```python
content = '''Hello 123456
World'''
pattern = '^He.*?(\d+).*ld'
```

>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>  File "<stdin>", line 1, in <lambda>
>AttributeError: 'NoneType' object has no attribute 'group'

原因是"."不能匹配换行符，所以我们这里需要使用re.S修饰，来使"."可以对换行符进行匹配

```python
result = re.match(pattern,content,re.S)
print(result.group(1))
```

> 123456

| 修饰符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| `re.I` | 使匹配对大小写不敏感                                         |
| `re.L` | 做本地化识别（locale-aware）匹配                             |
| `re.M` | 多行匹配，影响`^`和`$`                                       |
| `re.S` | 使`.`匹配包括换行在内的所有字符                              |
| `re.U` | 根据Unicode字符集解析字符。这个标志影响`\w`、`\W`、 `\b`和`\B` |
| `re.X` | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解 |

### 转义匹配

对于内容中，如果本身就含有"."之类特殊字符，对这些字符进行匹配则需要用到"`\`"

```python
import re 
content = '(谷歌)www.google.com'
pattern = '\(谷歌\)www\.google\.com'
result = re.match(pattern,content)
print(result)
```

> <_sre.SRE_Match object; span=(0, 18), match='(谷歌)www.google.com'>

## search()

相对match()仅能从头开始匹配，`search()`方法允许返回整个字符串第一个匹配的特征。

```python
import re 
content = '(谷歌)www.google.com'
pattern = 'www.(.*?).com'
result = re.search(pattern,content)
result.group(1)
```

> <_sre.SRE_Match object; span=(4, 18), match='www.google.com'>
>
> google

## findall()

需要通过一个特征匹配多组数据，`findall()`方法可以返回整个字符串所匹配的所有数据到列表中。

```python
import requests,re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
website = 'https://www.bilibili.com/read/home'
rget = requests.get(website,headers=headers,timeout=3)
pattern = '<span class="rank-index">(.*?)</span><a href="//www.bilibili.com/read/(.*?)/" target="_blank" title="(.*?)">(.*?)</a>'
results = re.findall(pattern,rget.text,re.S)
print(results)
```

> B站，你懂的，总有几个感觉不易于消化的内容，不放上来了，返回的是列表形式。

## sub()

将匹配的字符串直接进行替换，既可以用字符串提供的`replace()`方法，也可以使用re模块的`sub()`方法

`sub(repl, string[, count])`

count表示最多替换次数

```python
content = 'u 24a0r1e 9a4 ge3n3i123u55s'
content = re.sub('\d+','',content)
```

> 自己动手

- 提一点，在html,xml等等作为content层面上的应用，可以通过`sub()`方法将上级节点去掉，即替换为空
- `re.sub('<节点名.*>|</节点名.*>')`,'|'表示或。

## compile()

将一段正则表达式编译为**pattern**对象，并且可以传入修饰符，如re.S，从而不需要在使用`search()`、`findall()`等方法时再传入re.S了

```python
import re
content1 = '2018-09-16 12:00:00'
content2 = '''2018-09-17 12:00:00
2018-09-18 12:00:00'''
pattern = re.compile('\d{2}:\d{2}:\d{2}',re.S)
pattern = '\d{2}:\d{2}:\d{2}'
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
print('r1:{0}\nr2:{1}'.format(result1,result2))
```

>r1:2018-09-16
>r2:2018-09-17
>2018-09-18

## split()

由于某些情况需要按照某些特征作为分隔符，提取为列表数据，使用`split()`

```python
import re
content = '''2018-09-17 12:13:14
2018-09-18 12:18:07'''
pattern = re.compile('-|\s|:',re.S)
result = re.split(pattern,content)
print(result)
```

> ['2018', '09', '17', '12', '13', '14', '2018', '09', '18', '12', '18', '07']

- 针对时间的"-"，"空格"，":"作为分隔符提取
- 实际上\s并不需要，re.S也不需要，仅做列出方案