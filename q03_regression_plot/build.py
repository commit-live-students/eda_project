# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
plt.switch_backend('agg')
def regression_plot(variable1, variable2):
    plot = sns.lmplot(variable1, variable2, data, fit_reg=True)
    return plot
regression_plot('SalePrice', 'GrLivArea')






