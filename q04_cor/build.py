# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def cor(data):
    df_cor = data.corr()
    sns.heatmap(df_cor)
    plt.show()



