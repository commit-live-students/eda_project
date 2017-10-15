# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/house_prices_multivariate.csv')


X = data.LotArea[:,np.newaxis]  # Reshape
y = data.SalePrice
# Write your code here
def regression_plot(X,y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    y_pred = regressor.predict(X)
    plt.scatter(X, y)
    plt.plot(X, y_pred, "r-")
    plt.title('Housing Price ')
    plt.xlabel('Area')
    plt.ylabel('Price')
    plt.show()

#regression_plot(X,y)
