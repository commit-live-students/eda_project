# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(data):
    data.hist(['LotArea', 'GarageArea','OpenPorchSF','SalePrice'])
    plt.show()
