# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    num_cols=[data['LotArea'],data['GarageArea'],data['OpenPorchSF'],data['SalePrice']]
    Plot=plt.hist(num_cols, bins=50, alpha=0.5, label=['LotArea','GarageArea','OpenPorchSF','SalePrice'])

    plt.legend(loc='upper right')
    
    
    return Plot
    
    


