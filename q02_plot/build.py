# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
num_cols = ['LotArea','GarageArea','OpenPorchSF','SalePrice']
def plot(num_cols):
    cols = 2

    number_of_rows = len(num_cols)-1/cols
    plt.figure(figsize=(15,20))
    for i in range(0,len(num_cols)):
        plt.subplot(number_of_rows,cols,i+1)
        sns.boxplot(data[num_cols[i]].dropna())
    plt.tight_layout()
    plt.show()
