# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(var1,var2):
    sns.lmplot(x=var1,y=var2,data=data)




sns.lmplot(x='SalePrice',y='GrLivArea',data=data)
regression_plot('SalePrice','GrLivArea')


