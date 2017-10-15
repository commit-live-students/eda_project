# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here


#sns.lmplot(x='GrLivArea', y='SalePrice', data=data, fit_reg=True)
# Write your code here
def regression_plot(var1,var2):
    sns.lmplot(x=var1, y=var2, data=data, fit_reg=True)
    plt.show()
    return plt
