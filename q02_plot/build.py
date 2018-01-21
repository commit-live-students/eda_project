# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
num_cols = ['LotArea' ,'GarageArea','OpenPorchSF','SalePrice']
# Write your code here:

def plot(num_cols):
    fig, axs = plt.subplots(ncols=len(num_cols))
    for idx, val in enumerate(num_cols):
        sns.boxplot(x=data[val], ax=axs[idx])
    plt.show()
