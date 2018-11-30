# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')

# Write your code here
def regression_plot(a,b):
    sns.lmplot(a, b, data = data, fit_reg=True)
regression_plot('GrLivArea','SalePrice')






