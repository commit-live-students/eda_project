# %load q02_plot/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

cols = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']
# Write your code here:
def plot(num_cols):
    for i in range(0, len(num_cols), 2):
        if(i < len(num_cols)):
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(None, num_cols[i], data=data)
            plt.subplot(122)
            sns.boxplot(None, num_cols[i+1], data=data)
            plt.tight_layout()
            plt.show()

plot(['LotArea','GarageArea','OpenPorchSF','SalePrice'])

