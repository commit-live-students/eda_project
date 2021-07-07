# %load q02_plot/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here:
def plot(num_cols):
     _, args=plt.subplots(2,2)
     if num_cols>0:
        args[0,0].boxplot(data.LotArea)
     if num_cols>1:
        args[0,1].boxplot(data.GarageArea)
     if num_cols>2:
        args[1,0].boxplot(data.OpenPorchSF)
     if num_cols>3:
        args[1,1].boxplot(data.SalePrice)

plt.boxplot(data.GarageArea)
num_cols=10
_, args=plt.subplots(2,2)
if num_cols>0:
    args[0,0].boxplot(data.LotArea)
if num_cols>1:
    args[0,1].boxplot(data.GarageArea)
if num_cols>2:
    args[1,0].boxplot(data.OpenPorchSF)
if num_cols>3:
    args[1,1].boxplot(data.SalePrice)
plot(5)


