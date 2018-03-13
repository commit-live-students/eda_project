# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')

v1 = 'GrLivArea'
v2 = 'SalePrice'

def regression_plot(v1,v2):
    sns.lmplot(v1,v2,data,fit_reg=True)
    plt.show()

print regression_plot(v1,v2)
