import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(variable1, variable2):
    sns.jointplot(variable1, variable2, data=data, kind='reg')
    return plt.show()


