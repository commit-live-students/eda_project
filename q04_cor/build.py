# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(data):
    
    plt.figure(figsize=(12,8))
    sns.heatmap(data.corr())
    plt.show()
    
cor(data)






