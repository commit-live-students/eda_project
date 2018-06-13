# %load q01_plot/build.py
# Default imports

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = pd.read_csv('data/house_prices_multivariate.csv')
lst = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']

# Write your code here:
def plot(lst):
    for i in range(0,len(lst),2):
        if len(lst) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.distplot(data[lst[i]], kde=False)
            plt.subplot(122)
            sns.distplot(data[lst[i+1]], kde=False)
            plt.tight_layout()
            plt.show()
    return plt


