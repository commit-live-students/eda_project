# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(cols):
    a = []
    for i in range(0,len(cols)):
        a.append(sns.boxplot(data[cols[i]]))
        #plt.show()
    return a
