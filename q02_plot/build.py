# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
# Write your code here:
def plot(num_cols):
    for i in range(0,4,2):
        plt.figure(figsize=(10,4))
        plt.subplot(121)
        sns.boxplot(None, data[num_cols[i]])
        plt.subplot(122)
        sns.boxplot(None, data[num_cols[i+1]])
        plt.tight_layout()
        plt.show()

# print(plot(num_cols))
