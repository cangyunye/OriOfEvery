"""
功能：汇率换算
作者：輝
版本：1.0
日期：2017年12月8日
"""
#标题
print('汇率换算')
#人民币输入 input函数是以字符串形式赋值
rmb_str_value = input('人民币(CNY)金额：')
#汇率
usd_vs_rmb = 6.77 #人民币兑美元汇率
#将字符串转换为数字
rmb_str_value = eval(rmb_str_value)
#汇率计算
usd_value = rmb_str_value / usd_vs_rmb
#输出
print('美元(USD)金额是：',usd_value)
