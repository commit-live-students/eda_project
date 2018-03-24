# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

data = pd.read_csv('data/house_prices_multivariate.csv')
cols = data[['LotArea','GarageArea','OpenPorchSF','SalePrice']]
num_cols = len(cols.columns)

def plot(num_cols):
    for a in range(1,4):
        for n in range(0,num_cols):
            plt.subplot(num_cols,1,a)
            sns.boxplot(cols[cols.columns[n]])
            plt.show()
        return
