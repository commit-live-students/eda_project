import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(GrLivArea,SalePrice):
    sns.lmplot('GrLivArea', 'SalePrice', data=data, fit_reg=True)
    plt.show()
