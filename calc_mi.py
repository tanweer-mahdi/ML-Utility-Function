def calc_mi(X,y):
    X = X.copy()
    for column in X:
        if X[column].dtype == "object" or X[column].dtype == "O":
            X[column], _ = X[column].factorize()
    discrete = [X[i].dtype != 'float64' for i in X]
    mi_scores = mutual_info_regression(X,y,discrete_features=discrete, random_state=0)
    MI = {}
    for i, val in enumerate(X):
        MI[val] = mi_scores[i]
    return MI
