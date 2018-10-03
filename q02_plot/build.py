# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']

# Write your code here:

def plot(num_cols):
    facet = None
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(facet, num_cols[i],data = data)
            plt.subplot(122)            
            sns.boxplot(facet, num_cols[i+1],data = data)
            plt.tight_layout()
            plt.show()

<<<<<<< HEAD
=======

>>>>>>> 5493eb5222108eaac16816ee2491cb2f5a8dd598
plot(num_cols)


