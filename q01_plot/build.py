# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):   
    f, axes = plt.subplots(2, 2, figsize=(15, 12))
    sns.distplot(data['GarageArea'], ax = axes[0,0])
    sns.distplot(data['LotArea'], ax = axes[0,1])
    sns.distplot(data['OpenPorchSF'], ax = axes[1,0])
    sns.distplot(data['SalePrice'], ax = axes[1,1])
    plt.show()
    return plt
    

plot(data)



