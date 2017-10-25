# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

l1 = [1,25,27,34]
def plot(l1):

    a=l1[0]
    b=l1[1]
    c=l1[2]
    d=l1[3]
    x = data.iloc[:,a].values
    y = data.iloc[:,b].values
    z = data.iloc[:,c].values
    p = data.iloc[:,d].values
    fig, axes = plt.subplots(nrows=2, ncols=2)
    axes[0][0].hist(x)
    axes[0][1].hist(y)
    axes[1][0].hist(z)
    axes[1][1].hist(p)
    a1 = fig.show()
    return a
