# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    plt.boxplot(data['LotArea'],data['GarageArea'],data['OpenPorchSF'],data['SalePrice'])
    plt.show()
    return



