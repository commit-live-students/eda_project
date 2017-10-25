# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv('data/house_prices_multivariate.csv')


def regression_plot(a,b):
    return sns.lmplot(a,b,data,fit_reg=True)





regression_plot("GrLivArea","SalePrice")
