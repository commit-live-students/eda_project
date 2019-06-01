# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')


# Write your code here
def regression_plot(a,b):
    plt.scatter(a,b)
    return plt.show()

a=data['SalePrice']
b=data['GrLivArea']
regression_plot(a,b)


