# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(v1,v2):
    return sns.jointplot(data[v1],data[v2],data=data,kind='reg')
