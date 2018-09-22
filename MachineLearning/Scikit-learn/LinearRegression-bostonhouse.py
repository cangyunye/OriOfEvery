from sklearn import datasets
from sklearn.linear_model import LinearRegression
loaded_data = datasets.load_boston()
#特征数据
data_X = loaded_data.data
#返回属性
data_y = loaded_data.target
#线性回归模型
model = LinearRegression()
#拟合函数训练
model.fit(data_X,data_y)
#将采样数据data_X输入，predict返回属性
print(model.predict(data_X[:4,:]))
#打印实际数据，结果发现区别挺大的，所以，建议使用train_test_split将data分为test和train两部分随机再试一把
print(data_y[:4])
#打印因子系数
print("coefficient：",model.coef_)
print("interception：",model.intercept_)
#返回定义LinearRegression时的给定参数
print(model.get_params())
#将预测结果对比打分,获得准确度
print(model.score(data_X,data_y))