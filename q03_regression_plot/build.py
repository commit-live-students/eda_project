# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(GrLivArea, SalePrice):
    sns.lmplot(GrLivArea, SalePrice, data=dataframe, fit_reg=True)
    return plt.show()

#regression_plot('GrLivArea', 'SalePrice')

# Write your code here







