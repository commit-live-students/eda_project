# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


def plot(num_cols):
    plt.figure(figsize=(50,50))
    for i in range(len(num_cols)):
        col = num_cols[i]
        plt.subplot(len(num_cols), 1, i+1)
        sns.boxplot(data[col])
    plt.show()


