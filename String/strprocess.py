"""
string.capitalize() 把字符串的第一个字符大写
string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.decode(encoding='UTF-8', errors='strict')以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
string.encode(encoding='UTF-8', errors='strict')以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.startswith(obj, beg=0,end=len(string))检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.endswith(obj, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
string.find(str, beg=0, end=len(string))检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.rfind(str, beg=0,end=len(string) )反向find
string.index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.rindex( str, beg=0,end=len(string))反向index
string.isalnum()如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True
string.isalpha()如果 string 至少有一个字符并且所有字符都是字母则返回 True
string.isdecimal()如果 string 只包含十进制数字则返回 True
string.isdigit()如果 string 只包含数字则返回 True
string.islower()如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True
string.isupper()如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True
string.isnumeric()如果 string 中只包含数字字符，则返回 True
string.isspace()如果 string 中只包含空格，则返回 True
string.lower()转换 string 中所有大写字符为小写.
string.upper()转换 string 中的小写字母为大写
string.swapcase()翻转大小写
string.ljust(width)返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.rjust(width)右对齐
string.lstrip()截掉 string 左边的空格
string.rstrip()删除 string 字符串末尾的空格.
string.strip([obj])执行 lstrip()和 rstrip()
string.maketrans(intab, outtab])
---maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
string.partition(str)将字符串分为(str前,str,str后)
string.rpartition(str)(str后,str,str前)
string.replace(str1, str2,  num=string.count(str1))将str1替换为st2，num为最大替换次数
string.split(str="", num=string.count(str))	以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
string.splitlines(num=string.count('\n')) 按行分割
string.title()返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

"""
