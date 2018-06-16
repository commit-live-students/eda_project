# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']

def plot(num_cols):
    for i in range(len(num_cols)):
        plt.figure(figsize=(10,4))
        sns.distplot(data[num_cols[i]],kde=False)
        plt.show()
plot(num_cols)    


