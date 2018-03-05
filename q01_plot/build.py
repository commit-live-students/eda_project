import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
def plot(num_cols):
    for col in num_cols:
        sns.distplot(data[col],kde=False)
