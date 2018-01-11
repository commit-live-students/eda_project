# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
# Write your code here
sp = data['SalePrice']
gla = data['GrLivArea']

def regression_plot(sp,gla):
    #sns.regplot(x=gla,y=sp)
    sns.jointplot(gla,sp,kind='reg')
    plt.show()
    return
