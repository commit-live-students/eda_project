import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(data):
    plt.subplot(4,2,1)
    sns.distplot(data['LotArea'])
    plt.subplot(4,2,2)
    sns.distplot(data['GarageArea'])
    plt.subplot(4,2,3)
    sns.distplot(data['OpenPorchSF'])
    plt.subplot(4,2,4)
    sns.distplot(data['SalePrice'])
    plt.show()
    return 
