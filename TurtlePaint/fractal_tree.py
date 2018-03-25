"""
    功能：递归函数绘制分形树
    日期：2017年12月12日
"""
import random
import turtle
def colorful():
    cl = ('red','orange','yellow','green','blue','purple','pink','violet','grey','gold','darkblue')
    return cl[random.randrange(11)]
def draw_branch(branch_length):
    """
        分形树绘制
    """
    if branch_length >= 15:
        turtle.color('orange')
        #绘制中央树枝
        turtle.forward(branch_length)
        #绘制右侧树枝
        turtle.right(20)
        draw_branch(branch_length*0.8)
        #绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length*0.8)
        #返回中央树枝
        turtle.penup()
        turtle.right(20)
        turtle.backward(branch_length)
        turtle.pendown()
    elif branch_length >= 10 and branch_length < 15:
        turtle.color('green')
        #绘制中央树枝
        turtle.forward(branch_length)
        #绘制右侧树枝
        turtle.right(20)
        draw_branch(branch_length*0.8)
        #绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length*0.8)
        #返回中央树枝
        turtle.penup()
        turtle.right(20)
        turtle.backward(branch_length)
        turtle.pendown()
def main():
    turtle.left(90)
    turtle.pensize(3)
    draw_branch(40)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
