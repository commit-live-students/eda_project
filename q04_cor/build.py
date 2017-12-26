# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

numerics = ['LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt',
            'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
            'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
            'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
            'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars',
            'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
            'ScreenPorch', 'PoolArea', 'MiscVal', 'YrSold', 'SalePrice']

data = pd.read_csv('data/house_prices_multivariate.csv')
df_numerics = data[numerics]

# Write your code here
def cor(data):
    plt.figure(figsize=(12,8))
    sns.heatmap(df_numerics.corr(),cmap='viridis')
    return None
