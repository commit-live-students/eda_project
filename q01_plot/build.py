import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here :
def plot(l_cols):
    for col in l_cols:
        data.hist(column=col)
        plt.show()
