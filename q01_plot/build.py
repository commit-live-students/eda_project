# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):
    num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
    for i in range(0,len(num_cols),2):
        if len(num_cols)>i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.distplot(data[num_cols[i]], hist=True, kde=False)
            plt.subplot(122)
            sns.distplot(data[num_cols[i+1]], hist=True, kde=False)
            plt.tight_layout()
            plt.show()
        else:
            sns.distplot(data[num_cols[i]], hist=True, kde=False)




