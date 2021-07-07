# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):
    #data[num_cols].boxplot()
    for i in num_cols:
        sns.boxplot(data[i])
        plt.show()




