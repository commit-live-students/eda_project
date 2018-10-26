import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(v1, v2):
    v1, v2 = 'GrLivArea', 'SalePrice'
    sns.lmplot(v1, v2, data=dataframe, fit_reg=True)
    plt.show();
    







