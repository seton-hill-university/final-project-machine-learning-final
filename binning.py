# Ashly DeFalco
# final project
# binning

import pandas as pd

def binned(frame):

    file = frame

    # print("All unique values in action column", file['Action'].unique())
    # print(len(file['Action'].unique()))

    # Bin allow
    bin_allow_index = []
    for i in range(len(file)):
        if file['Action'].iloc[i] == 'allow':
            bin_allow_index.append(i)

    bin_allow = []
    for i in bin_allow_index:
        bin_allow.append(file.iloc[i])

    bin_allow = pd.DataFrame(bin_allow)
    #print("This is a bin for allow action\n", bin_allow)

    # Binning Deny

    bin_deny_index = []
    for i in range(len(file)):
        if file['Action'].iloc[i] == 'deny':
            bin_deny_index.append(i)

    bin_deny = []
    for i in bin_deny_index:
        bin_deny.append(file.iloc[i])

    bin_deny = pd.DataFrame(bin_deny)
    #print("This is a bin for deny action\n", bin_deny)

    # Bin drop

    bin_drop_index = []
    for i in range(len(file)):
        if file['Action'].iloc[i] == 'drop':
            bin_drop_index.append(i)

    bin_drop = []
    for i in bin_drop_index:
        bin_drop.append(file.iloc[i])

    bin_drop = pd.DataFrame(bin_drop)
    #print("This is a bin for drop action\n", bin_drop)

    # Bin reset-both
    bin_reset_both_index = []
    for i in range(len(file)):
        if file['Action'].iloc[i] == 'reset-both':
            bin_reset_both_index.append(i)

    bin_reset_both = []
    for i in bin_reset_both_index:
        bin_reset_both.append(file.iloc[i])

    bin_reset_both = pd.DataFrame(bin_reset_both)
    #print("This is a bin for reset-both action\n", bin_reset_both)

    frame = pd.concat([bin_allow, bin_deny, bin_drop, bin_reset_both], sort=False)

    return frame