# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    num_cols = [data.LotArea, data.GarageArea, data.OpenPorchSF, data.SalePrice]
    sns.boxplot(num_cols)
    show.plot()
