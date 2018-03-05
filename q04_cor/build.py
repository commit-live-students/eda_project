# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def cor(dt):
    plt.figure(figsize=(12,8))
    return sns.heatmap(dt.corr(), cmap='viridis')
