# Default imports

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
variable1 = data['SalePrice']
variable2 = data['GrLivArea']

def regression_plot(variable1,variable2):
    sns.regplot(variable2,variable1,fit_reg=True)
regression_plot(variable1,variable2)

# Write your code here
