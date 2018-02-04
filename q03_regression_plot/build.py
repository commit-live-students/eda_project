# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
def regression_plot(X,y):
    sns.regplot(X,y)
    plt.show()

# Write your code here
