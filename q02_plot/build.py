# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
plt.switch_backend('agg')
def plot(num_cols):
    for col in num_cols:
        sns.boxplot(x=data[col])
        plt.show()
num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
plot(num_cols)



