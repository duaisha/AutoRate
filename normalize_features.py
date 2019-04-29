import copy
from math import sqrt
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standard_scalar(train_data, test_data):
    scaler = StandardScaler()
    scaler = scaler.fit(train_data)
    X_train_normalized2 = scaler.transform(train_data)
    X_test_normalized2 = scaler.transform(test_data)
    return X_train_normalized2, X_test_normalized2

def minmax(train_data, test_data):
    scaler = MinMaxScaler()
    scaler = scaler.fit(train_data)
    X_train_normalized2 = scaler.transform(train_data)
    X_test_normalized2 = scaler.transform(test_data)
    return X_train_normalized2, X_test_normalized2

def intra_normalization(X_train, X_test):
    intra_train = copy.copy(X_train)
    intra_test = copy.copy(X_test)
    
    for i in range(X_train.shape[0]):
        intra_train[i,:,1:], intra_train[i,:,1:]= minmax(X_train[i,:,1:].astype(float).astype(int), X_train[i,:,1:].astype(float).astype(int))
        
    for j in range(X_test.shape[0]):
        intra_test[j,:,1:], intra_test[j,:,1:]= minmax(X_test[j,:,1:].astype(float).astype(int), X_test[j,:,1:].astype(float).astype(int))
    
    return intra_train, intra_test


def twod_threed(input_features, normalized_features):

    arr =[]; i=0
    
    for i in range(input_features.shape[0]):
        temp =[]; j =0 
        for j in range(52):
            #print(normalized_features[52*i+j,0])
            temp.append(normalized_features[52*i+j])

        arr.append(temp)

    return(np.array(arr))
    

def inter_normalization(X_train, X_test):
    
    inter_train=[]; inter_test = []
    
    inter_video_features2_train = copy.copy(X_train.reshape(X_train.shape[0]*X_train.shape[1], X_train.shape[2]))
    inter_video_features2_test = copy.copy(X_test.reshape(X_test.shape[0]*X_test.shape[1], X_test.shape[2]))
    
    inter_video_features3_train= copy.copy(inter_video_features2_train)
    inter_video_features3_test = copy.copy(inter_video_features2_test)
 
    inter_video_features3_train[:,1:],inter_video_features3_test[:,1:] = minmax(inter_video_features2_train[:,1:], inter_video_features2_test[:,1:])

    
    inter_train = twod_threed(X_train, inter_video_features3_train)
    inter_test = twod_threed(X_test, inter_video_features3_test)
    #print(inter_train)
    return inter_train, inter_test


