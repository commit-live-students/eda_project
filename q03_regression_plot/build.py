# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable1,variable2):
    variable1=data.loc[:,'SalePrice']

    variable2=data.loc[:,'GrLivArea']
    Plot=plt.scatter(variable1,variable2)
    return Plot





