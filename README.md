## ML-Utility-Function :rocket:
Repo of utility ML functions for some quick-dirty analysis

## calc_mi(X,y)
Returns a dictionary with variables as keys, mutual information as values. The dictionary is _unordered_.
`calc_mi(X,y)` takes care of the following issues under the hood:
1. Separates the floats variable. `sklearn.feature_selection` is used for calculating mutual information. It regards int64, int32 as a discrete object
2. Transform the `dtype('O')` (fancy way of saying string) variables
3. Calculates mutual information for each of the variables agaisnt the`y`

## top_n_features(MI,n)
Returns top `n` features from the feature score dictionary `MI` returned by `calc_mi(X,y)`
Plots top `n` features in descending order
