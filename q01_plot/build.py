# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    LotArea=data['LotArea']
    GarageArea=data['GarageArea']
    OpenPorchSF=data['OpenPorchSF']
    SalePrice=data['SalePrice']
    sns.distplot(LotArea, bins=25)
    sns.distplot(GarageArea, bins=25)
    sns.distplot(OpenPorchSF, bins=25)
    sns.distplot(SalePrice, bins=25)
    

