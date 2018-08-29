# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(ncols):
    for i in range(len(ncols)):
        plt.subplot2grid((1,3*len(ncols)),(0,3*i))
        sns.boxplot(data[ncols[i]],orient='v')
        plt.title(ncols[i])
    plt.show()

plot(['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice'])

