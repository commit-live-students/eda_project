# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    fig, ax = plt.subplots(figsize=(10,10))
    corr = data.corr()
    sns.heatmap(corr,ax=ax)
    plt.show()
cor(data)
