# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
def plot(num_col):
    for col in num_col:
        sns.boxplot(data[col])

# Write your code here:
