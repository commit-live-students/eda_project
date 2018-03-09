# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(list_columns):
    cols_in_input = len(list_columns)
    if cols_in_input < 3:
        total_cols = cols_in_input
        col_scale_factor = 6
    else:
        total_cols = 3
        col_scale_factor = 3
    rows = int(cols_in_input / total_cols) + 1
    plt.figure(figsize=(6*rows,col_scale_factor*total_cols))
    sns.set_style("darkgrid")
    for i in range(0,cols_in_input):
        plt.subplot(rows,total_cols,i+1)
        plt.title(list_columns[i])
        sns.boxplot(df.loc[:,list_columns[i]].dropna())
    plt.tight_layout()
    # plt.show()
    return plt
