# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(data):
    plt.subplot(4,2,1)
    sns.boxplot(y=data['LotArea'])
    plt.subplot(4,2,2)
    sns.boxplot(y=data['GarageArea'])
    plt.subplot(4,2,3)
    sns.boxplot(y=data['OpenPorchSF'])
    plt.subplot(4,2,4)
    sns.boxplot(y=data['SalePrice'])
    plt.show()
    return
