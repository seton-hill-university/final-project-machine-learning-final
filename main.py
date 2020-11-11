import pandas as pd
import random
file = 'finalData.csv'

def sample():
    #counting lines
    lines = sum(1 for i in open(file))
    #samplesize 10 x
    size = int(lines * 0.1)
    #Randomly skips rows. Only keep size rows. Keeps the header
    skip = random.sample(range(1,lines), lines - size)

    #removes every row in skip. faster loadtime
    data = pd.read_csv(file, skiprows=skip)
    print(data)

sample()