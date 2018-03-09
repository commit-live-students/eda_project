# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable_1, variable_2):
    sns.pairplot(df, x_vars=[variable_1, variable_2], y_vars=['SalePrice'], size=10, aspect=.8, kind="reg");
    plt.tight_layout()
    # plt.show()
    return plt
