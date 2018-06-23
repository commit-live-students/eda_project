# %load q03_regression_plot/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
# print(data['SalePrice'],data['GrLivArea'])

# Write your code here
def regression_plot(col1,col2):
    sns.lmplot(col1,col2,data=data, fit_reg=True)
    plt.show()
    
regression_plot('GrLivArea','SalePrice')





