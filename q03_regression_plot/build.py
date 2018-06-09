# %load q03_regression_plot/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable1, variable2):
    sns.lmplot(variable1, variable2, data=data, fit_reg=True)
    plt.show()
    




regression_plot('GrLivArea', 'SalePrice')


