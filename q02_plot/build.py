# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
    facet = None
    fig=plt.figure()
    for i in range(0,len(num_cols),2):
        if len(num_cols) >= i:
        
            plt.subplot(121)
            sns.boxplot(num_cols[i],data = dataframe)
            
            plt.subplot(122)            
            sns.boxplot( num_cols[i+1],data = dataframe)
            plt.tight_layout()
            return fig

        else:
            sns.boxplot(facet, num_cols[i],data = dataframe)
            return fig




