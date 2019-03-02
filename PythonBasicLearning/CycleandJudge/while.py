"""
功能：汇率换算
作者：輝
版本：2.0
日期：2017年12月8日
"""
#标题
print('汇率换算')
#汇率
usd_vs_rmb = 6.77 #人民币兑美元汇率
rmb_str_value = input('输入金额（如100USD):')
while rmb_str_value != 'Q':
    #获取金额单位
    unit = rmb_str_value[-3:]
    #获取金额
    money = eval(rmb_str_value[:-3])
    if unit == 'CNY':
        turnvalue = money / usd_vs_rmb
        print(unit,'换算USD金额为：',turnvalue)
    elif unit == 'USD':
        turnvalue = money * usd_vs_rmb
        print(unit,'换算CNY金额为：',turnvalue)
    else:
        print('输入错误')
    print('*******************************************')
    rmb_str_value = input('输入金额（如需退出，输入Q）:')
print('程序退出')
