# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
def cor(data):
    x=data.corr()
    sns.heatmap(x)
plt.show()
# Write your code here
