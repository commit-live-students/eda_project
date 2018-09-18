# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here

def regression_plot(var1=['SalePrice'],var2=['GrLivArea']):
    #sns.regplot(x=data['SalePrice'], y=data['GrLivArea']) 
    sns.lmplot(x='SalePrice',y='GrLivArea',data=df,size=12)

    return

#regression_plot(var1=['SalePrice'],var2=['GrLivArea'])

#sns.plt.show() 







