# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
variable2 = 'GrLivArea'
variable1 = 'SalePrice'

# Write your code here
def regression_plot(variable1, variable2):
    (sns.lmplot(variable1, variable2, data=data, scatter=True, fit_reg=True))
    return plt.show()



#print regression_plot(variable1, variable2)
