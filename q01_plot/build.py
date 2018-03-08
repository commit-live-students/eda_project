import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF','SalePrice']
def plot(num_cols):
    for n in num_cols:
        plt.subplot(2,2,1)
        plt.hist(n)
        plt.show()
