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
    cl = ('red','orange','yellow','green','blue','purple','dark','pink','violet','grey','gold','darkgreen')
    return cl[random.randrange(12)]
def pentagram(line,color):
    i = 5
    angle = 144
    turtle.pencolor(color)
    while i>0:
        turtle.forward(line)
        turtle.right(angle)
        i = i - 1
def main():
    i = 5
    line = 50
    turtle.pensize(3)
    while i > 0 :
        pentagram(line,colorful())
        i = i - 1
        line = line + 40
    turtle.exitonclick()
if __name__ == '__main__':
    main()
