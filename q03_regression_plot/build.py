# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(f1,f2):
    sns.regplot(f1,f2,data=data)
    plt.show()
# Write your code here
