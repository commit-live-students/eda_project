# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:

def plot(num_cols):
    plt.figure(figsize=(50, 50))
    plt.subplot(221)
    sns.distplot(data['LotArea'], bins=num_cols)
    plt.subplot(222)
    sns.distplot(data['GarageArea'], bins=num_cols)
    plt.subplot(223)
    sns.distplot(data['OpenPorchSF'], bins=num_cols)
    plt.subplot(224)
    sns.distplot(data['SalePrice'], bins=num_cols)
    plt.show()


