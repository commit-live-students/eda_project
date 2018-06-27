# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    plt.figure(figsize=(10,4))
    sns.boxplot(data['LotArea'])
    sns.boxplot(data['GarageArea'])
    sns.boxplot(data['OpenPorchSF'])
    sns.boxplot(data['SalePrice']) 
    plt.show()

plot(4)

