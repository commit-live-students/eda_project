# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

plt.switch_backend('agg')
# Write your code here
def regression_plot(variable1, variable2):
    
    return sns.regplot(data[variable1], data[variable2])



va1 = 'GrLivArea'
va2 = 'SalePrice'

regression_plot(va1,va2)


