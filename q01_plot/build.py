import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

col = ['LotArea','GarageArea','OpenPorchSF','SalePrice']

def plot(num_cols):
    noc = num_cols
    nor = int(len(col)/noc)
    plt.figure(figsize = (5*noc,5*nor))
    for i in range(0,len(col)):
        plt.subplot(nor+1,noc,i+1)
        sns.distplot(data[col[i]],kde= False)
    plt.show()

#print(plot(3))
