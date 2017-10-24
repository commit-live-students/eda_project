# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('agg')


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(x,y):
    plt.scatter(x,y)
    plt.show()

regression_plot(data['GrLivArea'],data['SalePrice'])
