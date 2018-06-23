# %load q04_cor/build.py
# Default imports
import matplotlib
matplotlib.use('agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here
def cor(data):
#     cm = data.columns
#     .corr()
#     print(cm)
#     cols = dataframe.corr().nlargest(k, 'SalePrice')['SalePrice'].index
#     cm = dataframe[cols].corr()
#     corrr = data[cm].cor()
#     print(data.corr())
#     plt.figure(figsize=(10,6))
    sns.heatmap(data.corr(),cmap='viridis')
    plt.show()
     
cor(data)




