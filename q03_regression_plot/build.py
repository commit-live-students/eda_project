# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here

def regression_plot(v1, v2):
    sns.regplot(x=v1, y=v2, data=data)
