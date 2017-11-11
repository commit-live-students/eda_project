# %load q04_cor/build.py
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
# Create a function cor(dataframe)
def cor(data):
    correlation_var = data.corr()
    sns.heatmap(correlation_var)
    plt.show()
    return
