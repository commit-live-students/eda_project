# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.switch_backend('agg')
data = pd.read_csv('data/house_prices_multivariate.csv')

liv = 'GrLivArea'
sale = 'SalePrice'
# Write your code here
def regression_plot(liv,sale):
    sns.jointplot(liv,sale,data=data,kind='reg')
    plt.show()
regression_plot(liv,sale)





