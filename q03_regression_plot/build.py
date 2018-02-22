# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
var1="GrLivArea"
var2="SalePrice"

def regression_plot(var1, var2):
    sns.jointplot(var1, var2, data=data, kind='reg')
    plt.show()
