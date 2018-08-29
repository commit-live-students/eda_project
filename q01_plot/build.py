# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(ncols):
    for i in range(len(ncols)):
        plt.subplot2grid((1,len(ncols)),(0,i))
        sns.distplot(data[ncols[i]])
    plt.show()
    

plot(['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice'])

