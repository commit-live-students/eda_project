# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
num_cols = [data['LotArea'], data['GarageArea'], data['OpenPorchSF'], data['SalePrice']]

def plot(num_cols):
    for n in num_cols:
       # LotArea = data['LotArea']
        plt.subplot(2,2,1)
        plt.hist(n)
        plt.show()
