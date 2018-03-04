import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
def plot(num_cols):
    cols = 3

    number_of_rows = len(num_cols)-1/cols
    plt.figure(figsize=(10,8))
    for i in range(0,len(num_cols)):
        plt.subplot(number_of_rows,cols,i+1)
        sns.distplot(data[num_cols[i]].dropna(),kde=False)
    plt.tight_layout()
    plt.show() 
