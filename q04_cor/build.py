# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
def cor(dataframe) :
    plt.figure(figsize=(12,8))
    sns.heatmap(dataframe.corr(), cmap='viridis')

# Write your code here
