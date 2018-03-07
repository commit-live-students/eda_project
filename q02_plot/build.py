# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
col = ['LotArea','GarageArea','OpenPorchSF','SalePrice']

def plot(num_cols):
    noc = num_cols
    nor = int(len(col)/noc)
    plt.figure(figsize = (5*noc,5*nor))
    for i in range(0,len(col)):
        plt.subplot(nor+1,noc,i+1)
        sns.boxplot(data[col[i]])
    plt.show()
    
#plot(3)




