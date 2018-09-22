# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
var1=['SalePrice']
var2=['GrLivArea']

def regression_plot(var1,var2):
    #sns.regplot(x=data['SalePrice'], y=data['GrLivArea']) 
    #g=sns.lmplot('SalePrice','GrLivArea',data)
    sns.lmplot(var1,var2,data)
    return

#regression_plot(var1=['SalePrice'],var2=['GrLivArea'])

#sns.plt.show() 







