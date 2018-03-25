"""
    功能：turtle函数绘制
    时间：2017年12月11日
"""
import random
import turtle
"""
turtle.forward() X轴向右
turtle.backward() X轴向左
turtle.right() 顺时针旋转角度
turtle.penup() 抬起画笔不绘制
turtle.pendown() 落笔可绘
turtle.pensize() 画笔宽度
turtle.pencolor() 画笔颜色
white,black,grey,darkgreen,gold,violet,purple
turtle.exitonclick()  点击关闭图形窗口
更多，参考https://docs.python.org/3.0/library/turtle.html
"""

def colorful():
    cl = ('red','orange','yellow','green','blue','purple','pink','violet','grey','gold','darkblue')
    return cl[random.randrange(11)]
def pentagram(line, color):
    side = 5
    angle = 144
    turtle.pensize(3)
    turtle.pencolor(color)
    while side>0:
        turtle.forward(line)
        turtle.right(angle)
        side = side - 1
def recursive_pentagram(line,stopline,step):
    pentagram(line, colorful())
    line += step
    if line <= stopline:
        recursive_pentagram(line,stopline,step)
def main():
    recursive_pentagram(40,120,30)
    turtle.exitonclick()
if __name__ == '__main__':
    main()
