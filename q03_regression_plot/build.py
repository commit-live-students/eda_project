# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')

# Write your code here
def regression_plot(feature1, feature2):
    plot = sns.lmplot(x=feature1, y=feature2, data=dataframe, size=12)
    return plot

regplot = regression_plot('SalePrice', 'GrLivArea')


