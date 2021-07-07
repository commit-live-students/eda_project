# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:

def plot(num_cols):
    fig, axes = plt.subplots(2, 2,)
    axes[0, 0].hist(data.LotArea,)
    axes[0, 1].hist(data.GarageArea)
    axes[1, 0].hist(data.OpenPorchSF)
    axes[1, 1].hist(data.SalePrice)
    plt.show()
plt.hist(data.GarageArea,bins=20)
fig, axes = plt.subplots(2, 2,)
axes[0, 0].hist(data.LotArea,)
axes[0, 1].hist(data.GarageArea)
axes[1, 0].hist(data.OpenPorchSF)
axes[1, 1].hist(data.SalePrice)
plt.show()
from inspect import getfullargspec
getfullargspec(plot)


