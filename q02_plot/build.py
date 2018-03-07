# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

facet = None

def plot(num_cols):

    num_of_rows = len(num_cols)/2
    for i in range(0, len(num_cols)):

        plt.subplot(num_of_rows+1, 2, i+1)
        sns.boxplot(facet, data[num_cols[i]])
        plt.tight_layout()

    plt.show()
