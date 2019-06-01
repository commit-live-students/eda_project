# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')
data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')


# Write your code here:
def plot(a):
    data.iloc[:,a[0]:a[0]+1].boxplot()
    data.iloc[:,a[1]:a[1]+1].boxplot()
    data.iloc[:,a[2]:a[2]+1].boxplot()
    data.iloc[:,a[3]:a[3]+1].boxplot()
    return plt.show()

a=[1,25,27,34]
plot(a)


