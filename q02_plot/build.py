# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    plt.boxplot(data['LotArea'])
    plt.show()
    plt.boxplot(data['GarageArea'])
    plt.show()
    plt.boxplot(data['OpenPorchSF'])
    plt.show()
    plt.boxplot(data['SalePrice'])
    plt.show()
