# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
def plot(num_cols):
        #num_cols = ['YearBuilt', 'TotalBsmtSF', 'GrLivArea', 'SalePrice']
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(data[num_cols[i]])
            plt.subplot(122)
            sns.boxplot(data[num_cols[i+1]])
            plt.tight_layout()
            plt.show()

        else:
            sns.boxplot(data[num_cols[i]])

# Write your code here:
