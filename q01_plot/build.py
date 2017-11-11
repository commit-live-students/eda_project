# %load q01_plot/build.py
'''Default Import'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
plot_data = data[['LotArea','GarageArea','OpenPorchSF','SalePrice']]
'''Write your code here'''
def plot(num_cols):
    plt.subplot(2,2,1)
    plot_data.LotArea.plot(kind='hist')
    plt.subplot(2,2,2)
    plot_data.GarageArea.plot(kind='hist')
    plt.subplot(2,2,3)
    plot_data.OpenPorchSF.plot(kind='hist')
    plt.subplot(2,2,4)
    plot_data.SalePrice.plot(kind='hist')
    plt.show()
    return
