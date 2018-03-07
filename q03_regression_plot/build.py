# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(variable1, variable2):

    sns.jointplot(data[variable1], data[variable2], kind = 'reg')
    plt.show()
