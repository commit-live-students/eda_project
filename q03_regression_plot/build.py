# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['YearBuilt', 'TotalBsmtSF', 'GrLivArea', 'SalePrice']

# Write your code here
def regression_plot(GrLivArea,SalePrice):
    sns.lmplot(GrLivArea,SalePrice, data=data, fit_reg=True)
    plt.show()

    







