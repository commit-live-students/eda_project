# %load q03_regression_plot/build.py
'''Default Import'''
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
# Create a function regression_plot(variable1, variable2) that returns a jointplot
def regression_plot(variable1,variable2):
    data.plot.scatter(x='GrLivArea',y='SalePrice')
    plt.show()
    return
