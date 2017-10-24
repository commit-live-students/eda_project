# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.pyplot.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    plt.subplot(2,2,1)
    sns.boxplot(data['LotArea'])
    plt.subplot(2,2,2)
    sns.boxplot(data['GarageArea'])
    plt.subplot(2,2,3)
    sns.boxplot(data['OpenPorchSF'])
    plt.subplot(2,2,4)
    sns.boxplot(data['SalePrice'])
    plt.show()

plot(len(data.columns))
