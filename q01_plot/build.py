import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):

    num_of_rows = len(num_cols)/2
    for i in range(0, len(num_cols)):

        plt.subplot(num_of_rows+1, 2, i+1)
        sns.distplot(data[num_cols[i]], bins = 20, kde = False)

    plt.show()
