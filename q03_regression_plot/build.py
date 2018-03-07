# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(SalePrice, GrLivArea):
     sns.regplot(x=data.GrLivArea, y=data.SalePrice, data=data)
     show.plot()
# Write your code here
