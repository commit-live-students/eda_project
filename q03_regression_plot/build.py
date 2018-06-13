# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
X = data.iloc[:,:-1]
y = data['SalePrice']
variable2 = 'SalePrice'
variable1 = 'GrLivArea'
# Write your code here
def regression_plot(variable1,variable2):
    return sns.lmplot(variable1,variable2, data=data)





