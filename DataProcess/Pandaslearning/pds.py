"""
    pandas数据分析
    pandas.series(list)#构建一维数组
        [属性]
        index获取索引号
        values获取数据
        head(n)预览前n条,默认n=5
        tail(n)预览后n条
        name
    pandas.DataFrame(list)#构建多维数组，操作方法类似dict
    sort_values(by='label')按值排序
    sort_index()按索引排序
    pandas.read_csv('filename')读取csv文件
    pandas.to_csv('filename',index=False)保存到csv文件且不带索引
    pandas.info()展示CSV基本信息，各字段总记录条数，字段类型
    pandas.dropna()丢弃缺失数据
    pandas.fillna()填充缺失数据
    [filter_condition]对数据进行过滤
    plot(kind,x,y,title,figsize)基于matplotlib,kind为图形,figsize为大小

"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    """
        主函数
    """

    aqi_data = pd.read_csv('AQI_v3.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())
    #数据调整，排除AQI为0部分
    aqi_data = aqi_data[aqi_data['AQI']>0]
    # 基本统计
    print('AQI最大值:', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)
    #绘制为图形
    top10_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的10个城市',
                      figsize=(20, 10))
    #保存图形
    plt.savefig('top10_aqi_bar.png')
    #展示图形
    plt.show()
    bottom10
    bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
