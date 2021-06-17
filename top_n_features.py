# plotting top n features

def top_n_features(MI,n):
    # MI is the dictionary of features and their corresponding MI scores
    # n is the number of features wanted
    tuples = list(zip(list(MI.keys()), list(MI.values()))) # tuple of features and their MIs
    tuples.sort(key=lambda x: x[1], reverse=True)
    if n > len(tuples): 
        print("There are only " + str(len(tuples)) + " features")
        return
    MI_topn = dict(tuples[:n])
    plt.figure(figsize=(13,13))
    plt.title("Top " + str(n) + " features")
    ax = sns.barplot(y= list(MI_topn.keys()), x = list(MI_topn.values()), orient='h')
    
    return MI_topn
