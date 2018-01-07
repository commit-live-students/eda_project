# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


def cor(data):
    k = 10 #number of variables for heatmap
    cols = data.corr().nlargest(k, 'SalePrice')['SalePrice'].index

    cm = data[cols].corr()
    plt.figure(figsize=(10,6))
    sns.heatmap(cm, annot=True, cmap = 'viridis')
    plt.show()
