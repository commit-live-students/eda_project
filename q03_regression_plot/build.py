# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
variable1 = data['SalePrice']
variable2 = data['GrLivArea']
def regression_plot(variable1,variable2):
    sns.regplot(variable1,variable2)
    plt.show()
