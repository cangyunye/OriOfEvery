> 在学会openpyxl基本操作之后，如何美化表格是一个很重要的课题

[TOC]

###样式(Styles)处理
##简介
样式常用来改变你的数据展示效果以及用于设定数字的格式。

样式可用于以下方面:

- 字体（font）中设置字体大小,颜色,下划线等等.
- 填充设置模式（pattern）或颜色（color）渐变
- 单元格边界（border）设置
- 单元格排版(alignment）
- 保护锁
  以下为默认设置
```python
>>> from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
>>> font = Font(name='Calibri',
...                 size=11,
...                 bold=False,
...                 italic=False,
...                 vertAlign=None,
...                 underline='none',
...                 strike=False,
...                 color='FF000000')
>>> fill = PatternFill(fill_type=None,
...                 start_color='FFFFFFFF',
...                 end_color='FF000000')
>>> border = Border(left=Side(border_style=None,
...                           color='FF000000'),
...                 right=Side(border_style=None,
...                            color='FF000000'),
...                 top=Side(border_style=None,
...                          color='FF000000'),
...                 bottom=Side(border_style=None,
...                             color='FF000000'),
...                 diagonal=Side(border_style=None,
...                               color='FF000000'),
...                 diagonal_direction=0,
...                 outline=Side(border_style=None,
...                              color='FF000000'),
...                 vertical=Side(border_style=None,
...                               color='FF000000'),
...                 horizontal=Side(border_style=None,
...                                color='FF000000')
...                )
>>> alignment=Alignment(horizontal='general',
...                     vertical='bottom',
...                     text_rotation=0,
...                     wrap_text=False,
...                     shrink_to_fit=False,
...                     indent=0)
>>> number_format = 'General'
>>> protection = Protection(locked=True,
...                         hidden=False)
>>>
```
###单元格样式和命名样式
样式有两种：单元格样式和命名样式（即样式模板）

##单元格样式
单元格样式在各对象之间是共享的，一旦被分配则无法更改，如此防止了不必要的副作用，比如说改变多个单元格的样式而非仅仅一对一个。
```python
>>> from openpyxl.styles import colors
>>> from openpyxl.styles import Font, Color
>>> from openpyxl import Workbook
>>> wb = Workbook()
>>> ws = wb.active
>>>
>>> a1 = ws['A1']
>>> d4 = ws['D4']
>>> ft = Font(color=colors.RED)
>>> a1.font = ft
>>> d4.font = ft
>>>
>>> a1.font.italic = True # 不允许
>>>
>>> # 如果你想改变字体的颜色，你需要重新分配font
>>>
>>> a1.font = Font(color=colors.RED, italic=True) # 本次改变仅对A1有效
```
###样式复制
样式也可以复制
```python
>>> from openpyxl.styles import Font
>>> from copy import copy
>>>
>>> ft1 = Font(name='Arial', size=14)
>>> ft2 = copy(ft1)
>>> ft2.name = "Tahoma"
>>> ft1.name
'Arial'
>>> ft2.name
'Tahoma'
>>> ft2.size # copied from the
14.0
```
###基本字体颜色
颜色(Colors)一般用RGB或16进制RGB表示，colors模块提供一些常量
```python
>>> from openpyxl.styles import Font
>>> from openpyxl.styles.colors import RED
>>> font = Font(color=RED)
>>> font = Font(color="FFBB00")
```
支持颜色索引(indexed)以及主题(theme)和调色(tint)
```python
>>> from openpyxl.styles.colors import Color
>>> c = Color(indexed=32)
>>> c = Color(theme=6, tint=0.5)
```
###样式应用
单元格应用样式
```python
>>> from openpyxl.workbook import Workbook
>>> from openpyxl.styles import Font, Fill
>>> wb = Workbook()
>>> ws = wb.active
>>> c = ws['A1']
>>> c.font = Font(size=12)
```
样式可以直接设置在行和列，但需要在Excel中，单元格已建好。如果你想在所有行列应用样式，那么你必须将样式应用于每个你所创建的单元格. 这是文件格式的限制:
```python
>>> col = ws.column_dimensions['A']
>>> col.font = Font(bold=True)
>>> row = ws.row_dimensions[1]
>>> row.font = Font(underline="single")
```
###对合并单元格样式化
有时候你想将一个范围的单元格当作一个对象来定义格式. Excel 可以通过合并单元格来操作(删除左上角以外其他格)然后为了应用伪样式，会重建单元格。
```python
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl import Workbook


def style_range(ws, cell_range, border=Border(), fill=None, font=None, alignment=None):
    """
    Apply styles to a range of cells as if they were a single cell.

    :param ws:  Excel worksheet instance
    :param range: An excel range to style (e.g. A1:F20)
    :param border: An openpyxl Border
    :param fill: An openpyxl PatternFill or GradientFill
    :param font: An openpyxl Font object
    """

    top = Border(top=border.top)
    left = Border(left=border.left)
    right = Border(right=border.right)
    bottom = Border(bottom=border.bottom)

    first_cell = ws[cell_range.split(":")[0]]
    if alignment:
        ws.merge_cells(cell_range)
        first_cell.alignment = alignment

    rows = ws[cell_range]
    if font:
        first_cell.font = font

    for cell in rows[0]:
        cell.border = cell.border + top
    for cell in rows[-1]:
        cell.border = cell.border + bottom

    for row in rows:
        l = row[0]
        r = row[-1]
        l.border = l.border + left
        r.border = r.border + right
        if fill:
            for c in row:
                c.fill = fill

wb = Workbook()
ws = wb.active
my_cell = ws['B2']
my_cell.value = "My Cell"
thin = Side(border_style="thin", color="000000")
double = Side(border_style="double", color="ff0000")

border = Border(top=double, left=thin, right=thin, bottom=double)
fill = PatternFill("solid", fgColor="DDDDDD")
fill = GradientFill(stop=("000000", "FFFFFF"))
font = Font(b=True, color="FF0000")
al = Alignment(horizontal="center", vertical="center")


style_range(ws, 'B2:F4', border=border, fill=fill, font=font, alignment=al)
wb.save("styled.xlsx")
```
###编辑页设置
```python
>>> from openpyxl.workbook import Workbook
>>>
>>> wb = Workbook()
>>> ws = wb.active
>>>
>>> ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
>>> ws.page_setup.paperSize = ws.PAPERSIZE_TABLOID
>>> ws.page_setup.fitToHeight = 0
>>> ws.page_setup.fitToWidth = 1
```
###命名样式
与单元格样式不同, 命名样式是可变的. 当你向一次应用于大量不同单元格时，这就给力了. NB. 如果将命名样式分配给一个单元格了，仅对单元格的额外部分更改，不影响单元格内容。

如果命名样式在一个workbook中注册了，那就可以直接通过名称关联。
##创建一个命名样式
```python
>>> from openpyxl.styles import NamedStyle, Font, Border, Side
>>> highlight = NamedStyle(name="highlight")
>>> highlight.font = Font(bold=True, size=20)
>>> bd = Side(style='thick', color="000000")
>>> highlight.border = Border(left=bd, top=bd, right=bd, bottom=bd)
```
建好的命名样式可以注册到workbook:
```python
>>> wb.add_named_style(highlight)
```
命名的样式也会在第一次被分配到一个单元格时自动注册：
```python
>>> ws['A1'].style = highlight
```
注册之后，可仅通过名称分配样式
```python
>>> ws['D5'].style = 'highlight'
```
###使用内置模块样式
该规范包括一些可以使用的内置样式. 然而，这些样式的名称存储在它们的本地化形式中. openpyxl只会识别英文名，而且只在这里写. 如下所示:

- ‘Normal’ # same as no style
##Number formats
- ‘Comma’
- ‘Comma [0]’
- ‘Currency’
- ‘Currency [0]’
- ‘Percent’
##Informative
- ‘Calculation’
- ‘Total’
- ‘Note’
- ‘Warning Text’
- ‘Explanatory Text’
##Text styles
- ‘Title’
- ‘Headline 1’
- ‘Headline 2’
- ‘Headline 3’
- ‘Headline 4’
- ‘Hyperlink’
- ‘Followed Hyperlink’
- ‘Linked Cell’
##Comparisons
- ‘Input’
- ‘Output’
- ‘Check Cell’
- ‘Good’
- ‘Bad’
- ‘Neutral’
##Highlights
- ‘Accent1’
- ‘20 % - Accent1’
- ‘40 % - Accent1’
- ‘60 % - Accent1’
- ‘Accent2’
- ‘20 % - Accent2’
- ‘40 % - Accent2’
- ‘60 % - Accent2’
- ‘Accent3’
- ‘20 % - Accent3’
- ‘40 % - Accent3’
- ‘60 % - Accent3’
- ‘Accent4’
- ‘20 % - Accent4’
- ‘40 % - Accent4’
- ‘60 % - Accent4’
- ‘Accent5’
- ‘20 % - Accent5’
- ‘40 % - Accent5’
- ‘60 % - Accent5’
- ‘Accent6’
- ‘20 % - Accent6’
- ‘40 % - Accent6’
- ‘60 % - Accent6’
- ‘Pandas’
  如果需要更多信息，请参考内置模块openpyxl.styles.builtins