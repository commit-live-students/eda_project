# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    i=0
    plt.figure(figsize=(10,4))
    plt.subplot(221)
    sns.distplot(data[num_cols[i]], hist=True, kde=True)
    plt.subplot(222)
    sns.distplot(data[num_cols[i+1]], hist=True, kde=True)
    plt.subplot(223)
    sns.distplot(data[num_cols[i+2]], hist=True, kde=True)
    plt.subplot(224)
    sns.distplot(data[num_cols[i+3]], hist=True, kde=True)

            #plt.tight_layout()
    plt.show()
