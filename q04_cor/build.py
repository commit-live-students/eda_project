# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')
data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')


# Write your code here
def cor(data):
    corr=data.corr()
    sns.heatmap(corr, xticklabels=corr.columns,yticklabels=corr.columns)
    return plt.show()

cor(data)


