# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.switch_backend('agg')
data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
facet = None
def plot(num_cols):
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(facet, num_cols[i],data = data)
            plt.subplot(122)            
            sns.boxplot(facet, num_cols[i+1],data = data)
            plt.tight_layout()
            plt.show()
plot(num_cols)



