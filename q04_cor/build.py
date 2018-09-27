# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
def cor(data):
    corr = data.corr()
    #print (corr)
    
    sns.set_context('notebook',font_scale = 1.0, rc = {'lines.linewidth':2.5})
    plt.figure(figsize = (13,7))
    a = sns.heatmap(corr, annot = True, fmt = '.2f')
    
    return

#cor(data)




