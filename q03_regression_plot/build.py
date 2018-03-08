# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable1,variable2):
    sns.regplot(x = data[variable1],y = data[variable2])
    plt.show()
