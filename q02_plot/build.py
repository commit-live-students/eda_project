# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

num_cols = ['LotArea', 'GarageArea', 'OpenPorchSF', 'SalePrice']
number_of_columns = 2
number_of_rows = (len(num_cols)-1) / number_of_columns
def plot(num_cols):
    for i in range(0, len(num_cols)):
        plt.subplot(number_of_rows+1, number_of_columns,i+1)
        sns.boxplot(data[num_cols[i]])
    plt.show()


