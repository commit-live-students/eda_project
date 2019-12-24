# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:


def plot(num_cols):
#    plt.hist()
#    plot = sns.distplot(data, kde=False, rug=True)
    sns.distplot( data['LotArea'] , color='skyblue', label='Lot Area')
    sns.distplot( data['GarageArea'] , color='red', label='Garage Area')
    sns.distplot( data['OpenPorchSF'] , color='green', label='Open Porch')
    sns.distplot( data['SalePrice'] , color='yellow', label='Sale P')

 #   return plot

    
num_cols = list([data['LotArea'],data['GarageArea'],data['OpenPorchSF'],data['SalePrice']]) 


