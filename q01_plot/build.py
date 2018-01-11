import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):
    #print data
    #print type(num_cols)
    #feature = data[num_cols]
    #for area in columns:
    #plt.hist([data.LotArea,data.GarageArea], color=['r','b'], alpha=0.5)
    #plt.hist(num_cols)
    #plt.hist(num_cols, color=['r','b','c','y'],alpha=0.5)
    #sns.distplot(num_cols,color=['r','b','c','y'])
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.distplot(data[num_cols[i]], kde=False)
            plt.subplot(122)
            sns.distplot(data[num_cols[i+1]], kde=False)
            plt.tight_layout()
            plt.show()

        else:
            sns.distplot(dataframe[num_cols[i]], kde=False)

    #plt.show()
    return

#data
num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
