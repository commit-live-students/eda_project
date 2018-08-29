# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(v1,v2):
    sns.regplot(data[v1],data['SalePrice'])
    plt.show()
    sns.regplot(data[v2],data['SalePrice'])
    plt.show()
    




regression_plot('SalePrice','SalePrice')

