
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
def regression_plot(variable1,variable2):
    plt.figure()
    sns.lmplot(variable1,variable2,data=data)
    plt.show()

#regression_plot('SalePrice','GrLivArea')
    







