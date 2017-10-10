# Draw a Scatter Plot to visualize the regression analysis

So, far we have only performed Univariate Analysis, now let's move into Multivariate Analysis.
Suppose you wanna know how is the `SalePrice` affected by the change in `GrLivArea`. Which can be achieved by using 
scatter plot as they used to show the relationship between two variables.
 
## Write a function `regression_plot` that :
- Plots a scatter plot for the variables using `seaborn` library
- Fits the linear regression line showing how the change in one variable affect the target variable `SalePrice`.

For these you don't need to load the data, we have already done it for you.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| variable1 |  | compulsory |  | name of the feature |
| variable2 |  | compulsory |  | name of the feature |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| Plot | | scatter plot for regression |
