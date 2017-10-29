# %load q04_cor/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')

def cor(data):
    return data[data.columns[1:]].corr()
# Write your code here


#cor(data)
