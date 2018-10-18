# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def cor(data):
    corr = data.corr()
    sns.set()
    ax = sns.heatmap(corr)
    return ax





