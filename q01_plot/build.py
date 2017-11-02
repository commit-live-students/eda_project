# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = [data['LotArea'],data['GarageArea'],data['OpenPorchSF'],data['SalePrice']]
# Write your code here:
def plot(num_cols):
    f,ax = plt.subplots(2, 2,figsize=(15,10))
    sns.distplot(num_cols[0],ax=ax[0,0])
    sns.distplot(num_cols[1],ax=ax[0,1])
    sns.distplot(num_cols[2],ax=ax[1,0])
    sns.distplot(num_cols[3],ax=ax[1,1])
    plt.show()
plot(num_cols)
