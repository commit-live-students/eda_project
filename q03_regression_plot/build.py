# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
sp=data.SalePrice
gla=data.GrLivArea
def regression_plot(gla,sp):
    sns.lmplot('GrLivArea','SalePrice',data=data)
    plt.show()
regression_plot(gla,sp)





