# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
plt.switch_backend('agg')


# Write your code here
def cor(data):
    sns.heatmap(data.cor())
    plt.show()
