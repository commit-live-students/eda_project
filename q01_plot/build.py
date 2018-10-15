# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import pandas as pd
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
def plot(a):
    num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.distplot(dataframe[num_cols[i]], kde=True)
            plt.subplot(122)            
            sns.distplot(dataframe[num_cols[i+1]], kde=True)
            plt.tight_layout()
            plt.show()

        else:
            sns.distplot(dataframe[num_cols[i]], kde=False)
           
plot(dataframe)


