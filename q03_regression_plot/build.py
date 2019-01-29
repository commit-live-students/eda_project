# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
variable1 = data['SalePrice']
variable2 = data['GrLivArea']




#
regression_plot(variable1, variable2)
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(variable1, variable2):
    sns.jointplot(variable1, variable2, data=data, kind='reg')
    return plt.show()


