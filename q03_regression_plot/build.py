# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here

def regression_plot(data):
    sns.lmplot('GrLivArea', 'SalePrice', data=data, fit_reg=True)
    plt.show()
    
