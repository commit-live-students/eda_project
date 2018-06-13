# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
lst = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']

# Write your code here:
def plot(lst):
    for i in range(0,len(lst),2):
        if len(lst) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(None, data[lst[i]], data=data)
            plt.subplot(122)
            sns.boxplot(None, data[lst[i+1]], data=data)
            plt.tight_layout()
            plt.show()


