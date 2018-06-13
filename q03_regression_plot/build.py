# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(x,y):
    
    sns.lmplot(x, y, data=data, fit_reg=True)
    plt.show()


regression_plot('GrLivArea','SalePrice')


