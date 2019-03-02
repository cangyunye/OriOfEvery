"""
    功能：BMR基础代谢率计算器
    版本：2017年12月13日
"""
def bmr_calc(gender,weight,height,age):
    if gender == '男':
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        bmr = -1
        print('暂时不支持该性别！')
    if bmr != -1:
        print('您的性别：{}\n您的体重：{}kg\n您的身高：{}cm\n您的年龄：{}cm\n基础代谢率为：{}大卡'.format(gender,weight,height,age,bmr))
        # print('您的性别：%s\n您的体重：%fkg\n您的身高：%fcm\n您的年龄：%dcm\n基础代谢率为：%f大卡' % (gender,weight,height,age,bmr))
        # #{0}可以按format中顺序输出，或者重复使用
        # print('您的性别：{0}\n您的体重：{1}kg\n您的身高：{2}cm\n您的年龄：{3}cm\n基础代谢率为：{4}大卡'.format(gender,weight,height,age,bmr))
def input_info1():
    while True:
        gender = input('性别：')
        weight = float(input('体重(kg)：'))
        height = float(input('身高(cm)：'))
        age = int(input('年龄：'))
        bmr_calc(gender,weight,height,age)
        state = input('Quit with Enter!>')
        if not state :
            break
def input_info2():
    person_info = input('性别  体重（kg） 身高（cm） 年龄\n')
    lst=person_info.split(' ')
    try:
        gender = lst[0]
        weight = float(lst[1])
        height = float(lst[2])
        age = int(lst[3])
        bmr_calc(gender,weight,height,age)
    except ValueError :
        print('请输入正确信息!')
    except IndexError :
        print('输入信息过少！')
    except :
        print('程序异常！')
# input_info1()
input_info2()
