# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
# Write your code here:
# %matplotlib inline

def plot(num_cols):
   
    f, axs = plt.subplots(2, 2, figsize=(7, 7), sharex=False)
    sns.boxplot(data['LotArea'],ax= axs[0,0])
    sns.boxplot(data['GarageArea'],ax=axs[0,1])
    sns.boxplot(data['OpenPorchSF'],ax=axs[1,0])
    sns.boxplot(data['SalePrice'],ax=axs[1,1])




