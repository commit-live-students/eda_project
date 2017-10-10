# Plot Histogram to get a sense of the distribution

We have already used the house pricing data for our in-class assignments. Now we will use the same data to solve some more assignments.
One of the best ways to get a sense for the variable distribution is to plot a histogram.

A Histogram gives us the representation of data by combining them into bins and drawing bars for 
each bin accordingly.
For this task you will need:- 
* `Matplotlib` which we have already used in Visualization 
* `Seaborn` which provides a high-level interface for drawing attractive statistical graphics. 

For this assignment you don't need to load the data, we have already done it for you.

## Write a function `plot` that :
- Plots a histogram for a distribution of the variables `LotArea` ,`GarageArea`, `OpenPorchSF`,`SalePrice`.
- Is able to show any skewness in the distribution.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| num_cols | list | compulsory |  | number of columns |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| Plot | | Histogram distribution for all given columns |

Let's get started