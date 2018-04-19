# %load q01_plot/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
columns = 2
rows = (len(num_cols)-1)/columns
def plot(num_cols):
    for i in range (0, len(num_cols)):
        plt.subplot(rows+1, columns, i+1)
        sns.distplot(data[num_cols[i]],kde=True)
        #plt.title(num_cols[i])
    plt.show()
#plot(num_cols)



