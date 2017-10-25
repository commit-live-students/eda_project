# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    axes[0][0].boxplot(x)
    axes[0][1].boxplot(y)
    axes[1][0].boxplot(z)
    axes[1][1].boxplot(p)
    a1=fig.show()
    return a1
