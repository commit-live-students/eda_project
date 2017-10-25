# Default imports
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    global data

    for i, col in enumerate(num_cols):
        plt.subplot(len(num_cols), 1 ,i+1)
        plt.hist(data[col])
    plt.show()
