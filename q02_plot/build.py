# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):

    facet = None
    i=0
    plt.figure(figsize=(10,4))
    plt.subplot(221)
    sns.boxplot(facet, num_cols[i],data = data)
    plt.subplot(222)
    sns.boxplot(facet, num_cols[i+1],data = data)
    plt.subplot(223)
    sns.boxplot(facet, num_cols[i+2],data = data)
    plt.subplot(224)
    sns.boxplot(facet, num_cols[i+3],data = data)


    plt.show()
    return plt
