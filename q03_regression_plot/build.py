# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')
x = data['GrLivArea']
y = data['SalePrice']

# Write your code here
def regression_plot(x,y):
    sns.lmplot('GrLivArea', 'SalePrice', data=data, fit_reg=True)
    
regression_plot(x,y)

