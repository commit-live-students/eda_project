# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import pylab as plt


import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    cols = data.corr()
    sns.heatmap(cols, annot=True, cmap = 'viridis')


