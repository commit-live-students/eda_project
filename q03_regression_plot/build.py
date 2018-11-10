# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(var1,var2):
    sns.lmplot('GrLivArea','SalePrice', data=data, fit_reg=True)
    plt.show()
    return(plt)



