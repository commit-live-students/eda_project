# %load q01_plot/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
cols = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']
# Write your code here:
def plot(num_cols):
    for i in range(0, len(num_cols), 2):
        if(i < len(num_cols)):
            plt.figure(figsize=(15,8))
            plt.subplot(121)
            sns.distplot(data[num_cols[i]],kde=True)
            plt.subplot(122)
            sns.distplot(data[num_cols[i+1]],kde=True)
            plt.show()
        



