# With this, we will build a decision tree and display the results using sklearn
import decisiontree
import entropy
import dimension
import euclidean
import binning

import pandas as pd
import numpy as np
import random

file = 'finalData.csv'


def sample():
    # counting lines
    lines = sum(1 for i in open(file))
    # samplesize 20 x
    size = int(lines * 0.2)
    # Randomly skips rows. Only keep size rows. Keeps the header
    skip = random.sample(range(1, lines), lines - size)

    # set column names for the dataset

    col_names = ['Source Port', 'Destination Port', 'NAT Source Port', 'NAT Destination Port', 'Action', 'Bytes',
                 'Bytes Sent', 'Bytes Received', 'Packets', 'Elapsed Time (sec)', 'pkts_sent', 'pkts_received']

    # removes every row in skip. faster loadtime
    data = pd.read_csv(file, skiprows=skip, header=0, names=col_names)
    return data


port_DATA = sample()

print("length: %s", len(port_DATA))

# Some of the values are reading as infinite. Replace with NaN
port_DATA.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop the Rows with NaN values
port_DATA.dropna(inplace=True)

port_DATA = binning.binned(port_DATA)

entropy.ent(port_DATA)

dimension.dim(port_DATA)

euclidean.euc(port_DATA)

decisiontree.decision_tree(port_DATA)
