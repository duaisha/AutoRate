import numpy as np
import csv
import sklearn


def confusion_matrix(rater_a, rater_b, min_rating=None, max_rating=None):
    """
    Returns the confusion matrix between rater's ratings
    """
    assert(len(rater_a) == len(rater_b))
    if min_rating is None:
        min_rating = min(rater_a + rater_b)
    if max_rating is None:
        max_rating = max(rater_a + rater_b)
    num_ratings = int(max_rating - min_rating + 1)

    conf_mat = [[0 for i in range(num_ratings)] for j in range(num_ratings)]
    for a, b in zip(rater_a, rater_b):
        #print(a,b)
        try:
            conf_mat[a - min_rating][b - min_rating] += 1
        except:
            print ("human score = " + str(a[0]) + " machine score = " + str(b))
    return conf_mat



def quadratic_weighted_kappa(rater_a, rater_b, min_rating=None, max_rating=None):
    k= rater_a.flatten()

    rater_a = np.array(rater_a, dtype=int)
    rater_b = np.array(rater_b, dtype=int)
    assert(len(rater_a) == len(rater_b))
    if min_rating is None:
        min_rating = min(min(rater_a), min(rater_b))
    if max_rating is None:
        max_rating = max(max(rater_a), max(rater_b))
    conf_mat = confusion_matrix(rater_a, rater_b,min_rating, max_rating)
    num_ratings = len(conf_mat)
    num_scored_items = float(len(rater_a))

    hist_rater_a = histogram(rater_a, min_rating, max_rating)
    hist_rater_b = histogram(rater_b, min_rating, max_rating)

    numerator = 0.0
    denominator = 0.0

    for i in range(num_ratings):
        for j in range(num_ratings):
            expected_count = (hist_rater_a[i] * hist_rater_b[j]
                              / num_scored_items)
            d = pow(i - j, 2.0) / pow(num_ratings - 1, 2.0)
            numerator += d * conf_mat[i][j] / num_scored_items
            denominator += d * expected_count / num_scored_items

    return 1.0 - numerator / denominator

def histogram(ratings, min_rating=None, max_rating=None):
    """
    Returns the counts of each type of rating that a rater made
    """
    if min_rating is None:
        min_rating = min(ratings)
    if max_rating is None:
        max_rating = max(ratings)
    num_ratings = int(max_rating - min_rating + 1)
    hist_ratings = [0 for x in range(num_ratings)]
    for r in ratings:
        try:
            hist_ratings[r - min_rating] += 1
        except:
            hist_ratings[r[0] - min_rating] += 1

    return hist_ratings


# In[53]:


def quadratic_kappa(arr, n_raters):

    kappa=[]
    sum1 = 0
    count = 0
    #print(arr.shape)
    for i in range(n_raters):
        j=i+1
        while (j< n_raters):
            count += 1
            sum1 += quadratic_weighted_kappa(arr[:,i],arr[:,j])
            kappa.append(quadratic_weighted_kappa(arr[:,i],arr[:,j]))
            j+=1
        
    avg = sum1/count
    #print(avg)
    return avg

