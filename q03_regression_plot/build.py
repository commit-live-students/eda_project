# Default imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here

def regression_plot(variable1, variable2):
    # scatter plot with variable against target and fit a line
    sns.lmplot(variable1, variable2, data=data, fit_reg=True)
    return None
# regression_plot('LotArea','SalePrice')
# regression_plot('MiscVal','SalePrice')
