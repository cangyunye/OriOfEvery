from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import l1_min_c
X,y = load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)
l2=LogisticRegression()
l2.fit(X,y)
print(l2.predict(X_test))
print(y_test)
print(l2.score(X_test,y_test))