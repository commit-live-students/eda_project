# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


def regression_plot(x,y):
    plt.scatter(x=x, y=y)
    plt.show()
