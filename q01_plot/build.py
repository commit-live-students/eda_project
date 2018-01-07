import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']


def plot(num_cols):
    fig, axs = plt.subplots(ncols=len(num_cols))
    for idx, val in enumerate(num_cols):
        sns.distplot(data[val], ax=axs[idx])

    plt.show()
