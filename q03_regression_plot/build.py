# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(dependent,independent):
    return sns.lmplot('GrLivArea','SalePrice',fit_reg=True,data=data)


