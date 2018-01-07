# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')
variable1="GrLivArea"
variable2="SalePrice"

def regression_plot(variable1, variable2):
    sns.jointplot(variable1, variable2, data=data, kind="reg")
    plt.show()
