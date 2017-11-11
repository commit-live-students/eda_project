# %load q02_plot/build.py
'''Default Import'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
housing_data = data[['LotArea','GarageArea','OpenPorchSF','SalePrice']]
# Create a function plot(num_cols) that returns a boxplot
# Write your code here
def plot(num_cols):
    sns.boxplot(data=housing_data)
    plt.show()
    return
