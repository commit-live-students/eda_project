# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

variable2 = 'SalePrice'
variable1 = 'GrLivArea'

# Write your code here
def regression_plot(variable1, variable2):
    sns.jointplot(variable1, variable2, data=data, kind='reg')
    return #plt.show()
