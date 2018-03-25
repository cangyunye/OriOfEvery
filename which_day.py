from datetime import datetime
def is_leap_year(year):
    #判断闰年
    if ((year % 400 ==0) or ((year % 4 == 0) and (year % 100 !=0) ) and month > 2):
        return True
    else:
        return False
def main():
    input_date_str = input('请输入日期(yyyy-mm-dd):\n')
    input_date = datetime.strptime(input_date_str,'%Y-%m-%d')
    # print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day
    #定义年度月份元组
    days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31,29)
    #定义年度月份列表
    days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31,29]
    #计算今日为本年第几天
    days = sum(days_in_month_tup[:month - 1]) + day
    # print(days_in_month_tup[:month - 1])
    #判断闰年
    if is_leap_year(year):
        days += 1
        #闰年，则2月含29日
        days_in_month_list[1]=29
    else:
        #非闰年，则还原
        days_in_month_list[1]=28
    daysl = sum(days_in_month_list[:month - 1]) + day
    print('现在是{}年，{}月，第{}天'.format(year,month,days))
    print('现在是{}年，{}月，第{}天'.format(year,month,daysl))
if __name__ == '__main__':
    main()
