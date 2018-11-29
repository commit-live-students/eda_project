# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#%matplotlib inline
plt.switch_backend('agg')
data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols=['LotArea','GarageArea','OpenPorchSF','SalePrice']

# Write your code here:
def plot(num_cols):
    for i in range(0,len(num_cols)):
        sns.distplot(data[num_cols[i]],kde=False)
        plt.show()
plot(num_cols)
    


