# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:

listie = [data.LotArea,data.GarageArea,data.OpenPorchSF, data.SalePrice]
def plot(num_cols):
    sns.set()
    ax = sns.displot(num_cols)
return ax



