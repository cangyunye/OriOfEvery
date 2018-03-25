"""
    功能：turtle函数绘制
    时间：2017年12月10日
"""
import turtle
"""
turtle.forward() X轴向右
turtle.backward() X轴向左
turtle.right() 顺时针旋转角度
turtle.exitonclick()  点击关闭图形窗口
"""
def main():
    i = 5
    while i>0:
        turtle.forward(300)
        turtle.right(144)
        i = i - 1
    turtle.exitonclick()
main()
