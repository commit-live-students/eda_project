import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

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
        sns.distplot(df.loc[:,list_columns[i]].dropna(),kde=True)
    plt.tight_layout()
    # plt.show()
    return plt
