# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:

num_cols = [data['LotArea'], data['GarageArea'], data['OpenPorchSF'], data['SalePrice']]

def plot(num_cols):
    for n in num_cols:
        plt.figure(figsize=(10,4))
        plt.subplot(121)
        sns.distplot(n, kde=False)
        plt.show()
