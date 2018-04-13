import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def cor(data):
    plt.figure(figsize=(15, 10))
    sns.heatmap(data.corr())
    return plt.show()


