# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:

def plot(l_cols):
    for col in l_cols:
        sns.boxplot(x=data[col], color="r")
        plt.show()
