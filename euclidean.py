# Euclidean Dist

import pandas as pd
import numpy as np

def euc (frame):

    df = frame

    # Defining two columns
    # Can use any two columns in the dataset
    Bytes_col = df["Bytes"]
    Packets_col = df["Packets"]

    # using zip to perform the Euclidean distance equation on two columns
    dist = np.sqrt(np.sum([(a - b) * (a - b) for a, b in zip(Bytes_col, Packets_col)]))

    print("Bytes Column")
    print(Bytes_col)

    print("Packets Column")
    print(Packets_col)

    print("\nEuclidean distance between two columns is:", dist)
    print("\n")