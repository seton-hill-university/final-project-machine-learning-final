# Ashly DeFalco
# final project
# binning

import csv
import pandas as pd
file = 'fileData.csv'

frame = pd.DataFrame()

def raw_data():
    raw_data = []
    with open("finalData.csv", "rb") as rawfile:
        reader = csv.reader(rawfile, delimiter=",")
        next(reader)
        for column in reader:
            raw_data.append(column)

    raw_data = pd.DataFrame(raw_data)
    return raw_data.T

#bin 1: allow
bin_allow_index=[]
for i in range (len(raw_data)):
    if raw_data['Action'].iloc[i] == 'allow':
        bin_allow_index.append(i)
bin_allow=[]
for i in bin_allow_index:
    bin_allow.append(raw_data.iloc[i])
bin_allow = pd.DataFreame(bin_allow)
bin_allow

#bin 2: dany
bin_deny_index=[]
for i in range (len(raw_data)):
    if raw_data['Action'].iloc[i] == 'deny':
        bin_deny_index.append(i)
bin_deny=[]
for i in bin_deny_index:
    bin_deny.append(raw_data.iloc[i])
bin_deny = pd.DataFreame(bin_deny)
bin_deny

#bin 3: drop
bin_drop_index=[]
for i in range (len(raw_data)):
    if raw_data['Action'].iloc[i] == 'drop':
        bin_drop_index.append(i)
bin_drop=[]
for i in bin_drop_index:
    bin_drop.append(raw_data.iloc[i])
bin_drop = pd.DataFreame(bin_drop)
bin_drop

#bin 4: reset-both
bin_reset_index=[]
for i in range (len(raw_data)):
    if raw_data['Action'].iloc[i] == 'reset':
        bin_reset_index.append(i)
bin_reset=[]
for i in bin_reset_index:
    bin_reset.append(raw_data.iloc[i])
bin_reset = pd.DataFreame(bin_reset)
bin_reset

raw_data=pd.read_csv(file, 'Action')
print(len(raw_data))