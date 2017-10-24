# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib
matplotlib.pyplot.switch_backend('agg')

data = pd.read_csv('data/house_prices_multivariate.csv')

# Write your code here:
def plot(num_cols):
    plt.subplot(2,2,1)
    plt.hist(data['LotArea'])
    plt.subplot(2,2,2)
    plt.hist(data['GarageArea'])
    plt.subplot(2,2,3)
    plt.hist(data['OpenPorchSF'])
    plt.subplot(2,2,4)
    plt.hist(data['SalePrice'])
    plt.show()
    
plot(len(data.columns))
