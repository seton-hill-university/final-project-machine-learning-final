import pandas as pd
import numpy as np

from sklearn.model_selection import KFold, cross_val_score, cross_val_predict


# Created testing and training data using K-Fold Cross validation
# Each fold has a testing set of 10% of the Full set
# Training set for each fold consists of the remaining 90%

def kfold(frame):
    df = frame

    dFeature = ['Source Port', 'Destination Port', 'Packets', 'pkts_received', 'Bytes', 'Bytes Received']

    X = np.array(df[dFeature])

    dTarget = ['Action']

    Y = np.array(df[dTarget])

    fold10 = KFold(n_splits=10)

    for train_index, test_index in fold10.split(X):
        x_train, x_test = X[train_index], X[test_index]

    for train_index, test_index in fold10.split(Y):
        y_train, y_test = Y[train_index], Y[test_index]

    return x_train, x_test, y_train, y_test

    # Fold 1
    test1 = df[:1315]
    training1 = df[1315:13105]

    # Fold 2
    test2 = df[1316:13106]
    training2 = df.loc[np.r_[0:1316, 2625:13105], :]

    # Fold 3
    test3 = df[2625:3935]
    training3 = df.loc[np.r_[0:2625, 3935:13105], :]

    # Fold 4
    test4 = df[3935:5245]
    training4 = df.loc[np.r_[0:3935, 5245:13105], :]

    # Fold 5
    test5 = df[5245:6555]
    training5 = df.loc[np.r_[0:5245, 6555:13105], :]

    # Fold 6
    test6 = df[6555:7865]
    training6 = df.loc[np.r_[0:6555, 7865:13105], :]

    # Fold 7
    test7 = df[7865:9175]
    training7 = df.loc[np.r_[0:7865, 9175:13105], :]

    # Fold 8
    test8 = df[9175:10485]
    training8 = df.loc[np.r_[0:9175, 10485:13105], :]

    # Fold 9
    test9 = df[10485:11795]
    training9 = df.loc[np.r_[0:10485, 11795:13105], :]

    # Fold 10
    test10 = df[11795:13105]
    training10 = df[:13105]
    print(training10)