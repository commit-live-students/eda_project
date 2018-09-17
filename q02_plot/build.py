# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(a):
  return sns.boxplot('GarageArea','SalePrice', data = dataframe)
plot(dataframe)



