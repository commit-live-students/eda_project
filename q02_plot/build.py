# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(data):
    x = np.random.normal(size=100)
    sns.distplot(x, kde=False);
    num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
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
            sns.distplot(data[num_cols[i]], kde=False)
