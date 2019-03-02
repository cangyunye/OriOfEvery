"""
    AQI计算
"""
def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        IAQI基本公式
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi
def cal_pm_iaqi(pm_val):
    """
        计算PM2.5 IAQI
    """
    if 0 <= pm_val < 35:
        iaqi = cal_linear(0,50,0,35,pm_val)
    elif 35 <= pm_val < 75:
        iaqi = cal_linear(50,100,35,75,pm_val)
    elif 75 <= pm_val < 115:
        iaqi = cal_linear(100,150,75,115,pm_val)
    elif 115 <= pm_val < 150:
        iaqi = cal_linear(150,200,115,150,pm_val)
    return iaqi
def cal_co_iaqi(co_val):
    """
        计算CO IAQI
    """
    if 0 <= co_val < 35:
        iaqi = cal_linear(0,50,0,2,co_val)
    elif 35 <= co_val < 75:
        iaqi = cal_linear(50,100,2,4,co_val)
    elif 75 <= co_val < 115:
        iaqi = cal_linear(100,150,4,14,co_val)
    elif 115 <= co_val < 250:
        iaqi = cal_linear(150,200,14,24,co_val)
    return iaqi
def cal_aqi(param_list):
    """
        AQI计算
    """
    #读取AQI列表param_list中各元素
    pm_val = param_list[0]
    co_val = param_list[1]
    #根据提供因子IAQI分别计算各分组IAQI
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)
    print('Step3:\npm_iaqi=%3d,co_iaqi=%3d' % (pm_iaqi,co_iaqi))
    #将IAQI搜集到列表
    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)
    print('Step4:\niaqi_list=',iaqi_list)
    #计算AQI
    aqi = max(iaqi_list)
    return aqi
def main():
    """
        主函数
    """
    print('请输入质量浓度，用空格分割')
    #仅输入2种因子的IAQI
    input_str = input('(1)PM2.5 (2)CO:\n')
    #通过空格区分两种元素，并分割成字符串
    str_list =  input_str.split(' ')
    #转换为float形式
    pm_val = float(str_list[0])
    co_val = float(str_list[1])
    print('Step1:\npm_val=%3d,co_val=%3d' % (pm_val,co_val))
    #构建AQI列表，记录各种因子AQI
    param_list = []
    #追加pm2.5
    param_list.append(pm_val)
    #追加co
    param_list.append(co_val)
    print('Step2:\nparam_list=',param_list)
    #调用AQI计算函数
    aqi_val = cal_aqi(param_list)
    print('空气质量指数为：{}'.format(aqi_val))
if __name__ == '__main__':
    main()
