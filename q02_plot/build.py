# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=False)
    sns.boxplot(data['LotArea'],ax= axes[0,0])
    sns.boxplot(data['GarageArea'],ax=axes[0,1])
    sns.boxplot(data['OpenPorchSF'],ax=axes[1,0])
    sns.boxplot(data['SalePrice'],ax=axes[1,1])
    return plt.show()
plot(3)


