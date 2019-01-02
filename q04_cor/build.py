# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    
    corr = data.corr()
    plot = sns.heatmap(corr, xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
    return plot




