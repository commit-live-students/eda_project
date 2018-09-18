# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(variable1='GrLivArea',variable2='SalePrice'):
#     sns.stripplot(x=variable1,y=variable2,data=data)
#     plt.show()
    sns.regplot(x=variable1, y=variable2,data=data)
    plt.show()



c=regression_plot(variable1='GrLivArea',variable2='SalePrice')


