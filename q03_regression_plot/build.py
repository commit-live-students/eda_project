# %load q03_regression_plot/build.py
# Default imports

import matplotlib
matplotlib.use('agg')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here

def regression_plot (variable1, variable2):
    return sns.lmplot(variable1,variable2, data=data, fit_reg=True)


#regression_plot('SalePrice','GrLivArea')
#plt.show()





