# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/house_prices_multivariate.csv')
#plt.switch_backend('agg')

# Write your code here:

plot_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']

def plot(num_cols):
    facet = None
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(facet, num_cols[i],data = df)
            plt.subplot(122)            
            sns.boxplot(facet, num_cols[i+1],data = df)
            plt.tight_layout()
            plt.show()


plot(plot_cols)


