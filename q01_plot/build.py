# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
plt.switch_backend('agg')
def plot(num_cols):
    for col in num_cols:
        sns.distplot(data[col], kde=True)
        plt.show()

num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
plot(num_cols)


