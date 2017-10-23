# Default imports

# %load q03_regres90sion_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = pd.read_csv('data/house_prices_multivariate.csv')
def regression_plot(variable1,variable2):

    sns.lmplot(dataframe[variable1], dataframe[variable2], data=dataframe, fit_reg=True)

#regression_plot(GrLivArea,SalePrice)



# Write your code here







# Write your code here
