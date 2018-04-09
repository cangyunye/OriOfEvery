
print('汇率转换')

rmb_str_value = input('请输入带单位金额如（100USD):')
usd_vs_rmb = 6.77
unit = rmb_str_value[-3:]
money = eval(rmb_str_value[:-3])

if unit == 'CNY':
    turnvalue = money / usd_vs_rmb
    print(unit,'转成USD后为',turnvalue)
elif unit == 'USD':
    turnvalue = money * usd_vs_rmb
    print(unit,'转成CNY后为',turnvalue)
else:
    print('输入错误！')

#如下只打印teenager，不进行更多判断
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
