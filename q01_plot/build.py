import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(cols):
    a = []
    for i in range(0,len(cols)):
        a.append(sns.distplot(data[cols[i]], kde=False))
        #plt.show()
    return a
