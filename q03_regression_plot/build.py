# %load q03_regression_plot/build.py
# Default imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
def regression_plot(variable1, variable2):
    sns.lmplot(variable1, variable2, data=data, fit_reg=True)


