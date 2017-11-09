# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
num_cols = data[['LotArea','GarageArea','OpenPorchSF','SalePrice']]

def plot(num_cols):
    plt.subplot(2,2,1)
    plt.hist(num_cols['LotArea'])
    plt.subplot(2,2,2)
    plt.hist(num_cols['GarageArea'])
    plt.subplot(2,2,3)
    plt.hist(num_cols['OpenPorchSF'])
    plt.subplot(2,2,4)
    plt.hist(num_cols['SalePrice'])
    plt.show()
