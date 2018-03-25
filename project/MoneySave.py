"""
    功能：每周存钱
    版本：2017-12-15
"""
import math
def save_money_in_weeks():
    amt = int(input('请输入开始的存入金额：'))
    increase_money = int(input('请输入金额递增数：'))
    total_weeks = int(input('请输入总共存钱周数：'))
    money_list = []
    total_money=0
    for current_week in range(total_weeks):
        money_list.append(amt)
        total_money = total_money + amt
        print('第{}周，存入{}，账户累计{}'.format(current_week+1,amt,total_money))
        amt += increase_money
        current_week += 1
    print(math.fsum(money_list))

def save_money1():
    increase_money=10 #每周存入金额增长值
    amt=10 #每周金额存入值
    total_money=0 #累计金额
    total_weeks=52  #总共存钱周数
    current_week=1 #当前周
    money_list = [] #设定存钱列表
    while current_week <= total_weeks:
        money_list.append(amt)
        total_money = total_money + amt
        print('第{}周，存入{}，账户累计{}'.format(current_week,amt,total_money))
        amt += increase_money
        current_week += 1
    print(math.fsum(money_list))

def save_money2():
    increase_money=10 #每周存入金额增长值
    amt=10 #每周金额存入值
    total_money=0 #累计金额
    money_list = [] #设定存钱列表
    for current_week in range(52):
        money_list.append(amt)
        total_money = total_money + amt
        print('第{}周，存入{}，账户累计{}'.format(current_week+1,amt,total_money))
        amt += increase_money
        current_week += 1
    print(math.fsum(money_list))


#save_money1()
#save_money2()
save_money_in_weeks()
