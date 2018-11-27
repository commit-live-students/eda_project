# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# plt.switch_backend('agg')

df = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(feature1,feature2):
    sns.jointplot(feature1, feature2, data=df, kind='reg')
    plt.show()
    

regression_plot('GrLivArea','SalePrice')


