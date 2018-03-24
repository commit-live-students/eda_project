# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
cols = data[['LotArea','GarageArea','OpenPorchSF','SalePrice']]
num_cols = len(cols.columns)

def plot(num_cols):
    for a in range(1,4):
        for n in range(0,num_cols):
            plt.subplot(2,num_cols,a)
            sns.distplot(cols[cols.columns[n]])
            plt.show()
        return
