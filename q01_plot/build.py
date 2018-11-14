# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    for i in range(len(num_cols)):
        sns.distplot(data[num_cols[i]])
    return plt.show()
    

columns = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']
plot(columns)


