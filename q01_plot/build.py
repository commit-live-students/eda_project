# Default imports
from inspect import getargspec
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def plot(num_cols) :

    dataframe = pd.read_csv('data/house_prices_multivariate.csv')
   # num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']

    num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.distplot(dataframe[num_cols[i]], kde=False)
            plt.subplot(122)
            sns.distplot(dataframe[num_cols[i+1]], kde=False)
            plt.tight_layout()
            plt.show()

        else:
            sns.distplot(dataframe[num_cols[i]], kde=False)
##plot()

# Write your code here:
