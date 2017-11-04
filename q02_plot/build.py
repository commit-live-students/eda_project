# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches(20, 10)
    for i, ax in enumerate(axes.flatten()):
        sns.boxplot(x=data.iloc[:, i], orient='h', ax=ax)
    return fig
