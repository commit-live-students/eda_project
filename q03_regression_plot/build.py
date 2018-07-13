# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
variable1 = data['SalePrice']
variable2 = data['GrLivArea']

# Write your code here
def regression_plot(variable1,variable2):
    sns.lmplot(variable2,variable1,data=data,fit_reg=True)
    return
    






