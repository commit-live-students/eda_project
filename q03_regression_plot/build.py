# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
x,y = 'GrLivArea', 'SalePrice'
def regression_plot(x,y):
#sns.lmplot('GrLivArea', 'SalePrice', data, fit_reg=True)
# Write your code here
    sns.jointplot(x,y, data=data, kind='reg')
    plt.show()

# regression_plot(x,y)
