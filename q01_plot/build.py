import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')

# Write your code here :
def plot(num_cols):
    plt.hist(num_cols)
    plt.show()
