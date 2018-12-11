# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')


data = pd.read_csv('data/house_prices_multivariate.csv')

v1 = data['SalePrice']
v2 = data['GrLivArea']
# Write your code here

def regression_plot(v1, v2):
    sns.regplot(x=v2,y=v1)
    plt.show()



regression_plot(v1, v2)


