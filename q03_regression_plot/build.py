# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here

X = 'GrLivArea'
y = 'SalePrice'

def regression_plot(X,y):

    sns.lmplot(X,y,data=data,fit_reg=True)
    plt.show()



