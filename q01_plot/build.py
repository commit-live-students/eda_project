# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
% matplotlib inline

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols=list(data)

def plot(num_cols):

#     for i in range(0,len(num_cols),2):
#         if len(num_cols) > i+1:
#             plt.figure(figsize=(10,4))
#             plt.subplot(121)
#             sns.distplot(data[num_cols[i]], kde=False)
#             plt.subplot(122)
#             sns.distplot(data[num_cols[i+1]], kde=False)
#             plt.tight_layout()
#             plt.show()

#         else:
#             sns.distplot(data[num_cols], kde=False)  
    f, axes = plt.subplots(2, 2, figsize=(13,13), sharex=False)
    sns.distplot( data['LotArea'] , color='skyblue', ax=axes[0, 0])
    sns.distplot( data['GarageArea'] , color='olive', ax=axes[0, 1])
    sns.distplot( data['OpenPorchSF'] , color='gold', ax=axes[1, 0])
    sns.distplot( data['SalePrice'] , color='teal', ax=axes[1, 1])
    
    plt.show()
c=plot(num_cols)



