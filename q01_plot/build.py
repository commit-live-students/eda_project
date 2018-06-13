# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    for i in range(0,len(num_cols),2):
        plt.figure(figsize=(10,4))
        plt.subplot(121)
        p = sns.distplot(data[num_cols[i]], kde=False)
        plt.subplot(122)
        sns.distplot(data[num_cols[i+1]], kde=False)
        plt.tight_layout()
        plt.show()
    return p



