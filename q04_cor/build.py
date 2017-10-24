# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.pyplot.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def cor(df):
    corr = df.corr()
    sns.heatmap(corr)
    plt.show()

cor(data)
