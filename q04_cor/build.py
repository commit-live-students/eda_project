# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
def cor(data):
    correlation = data.corr()
    sns.heatmap(correlation, vmin = -1, vmax = 1)
    plt.show()

# Write your code here
