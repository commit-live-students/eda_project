# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['LotArea' ,'GarageArea', 'OpenPorchSF','SalePrice']
number_of_columns = 2
number_of_rows = (len(num_cols)-1)/number_of_columns
def plot(num_cols):
    for i in range (0, len(num_cols)):
        plt.subplot(number_of_rows+1, number_of_columns, i+1)
        sns.distplot(data[num_cols[i]],kde=True,)
    plt.show()



# Write your code here :
