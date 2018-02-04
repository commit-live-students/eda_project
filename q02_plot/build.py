# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):
    for d in num_cols:
        sns.boxplot(data.iloc[:,d])
        plt.show()
# Write your code here:

# Write your code here:
