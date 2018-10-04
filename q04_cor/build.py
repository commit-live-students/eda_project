# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')

# Write your code here
def cor(df):
    plt.figure(figsize=(12,8))
    plot = sns.heatmap(df.corr(), annot=True, cmap='viridis')
    return plot

cor(data)


