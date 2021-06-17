## ML-Utility-Function
Repo of utility ML functions for some quick-dirty analysis

## calc_mi(X,y)
`calc_mi(X,y)` takes care of the following issues under the hood:
1. Separates the floats variable. `sklearn.feature_selection` is used for calculating mutual information. It regards int64, int32 as a discrete object
2. Transform the `dtype('O')` (fancy way of saying string) variables
3. Calculates mutual information for each of the variables agaisnt the`y`

