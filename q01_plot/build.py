import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


def plot(num_cols):
    for i in num_cols:
        plt.hist(i)
        plt.show()
