# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    sns.heatmap(data.corr())
    plt.show()

cor(data)

