# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    data = pd.read_csv('data/house_prices_multivariate.csv')
    for i in range(0, len(num_cols)):
        column = num_cols[i]
        sns.boxplot(x=data[column])


