# %load q04_cor/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    sns.heatmap(data.corr(),cmap='viridis')
    plt.show()


cor(data)


