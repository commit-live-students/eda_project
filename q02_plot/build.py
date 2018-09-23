# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
listie = [data.LotArea, data.GarageArea, data.OpenPorchSF, data.SalePrice]
def plot(num_cols):
    plt.rcParams['figure.figsize'] = (23,10)
    bx = sns.boxplot(x = num_cols , y = 'SalePrice', data = data)
    return bx



# Write your code here:




