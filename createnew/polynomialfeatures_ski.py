
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3,2)
pl = PolynomialFeatures(degree=2,interaction_only=False,include_bias=True)
pl.fit_transform(X)
pl.fit(X)