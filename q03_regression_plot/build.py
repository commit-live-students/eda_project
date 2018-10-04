# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#plt.switch_backend('agg')


data = pd.read_csv('data/house_prices_multivariate.csv')


variable1=  data.GarageArea
variable2=  data.GrLivArea

# Write your code here
def regression_plot(variable1,variable2):
    sns.regplot(variable1,data.SalePrice)
    plt.show()
    sns.regplot(variable2,data.SalePrice)
    plt.show()


