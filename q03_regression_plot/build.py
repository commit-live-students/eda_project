# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here

X = data.GrLivArea
Y = data.SalePrice
def regression_plot(X, Y):
    sns.set(color_codes=True)
    tips = sns.load_dataset(data)
    ax = sns.regplot(x=X, y=Y, data=tips)
    return ax







