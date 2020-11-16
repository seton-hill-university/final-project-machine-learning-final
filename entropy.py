import math
import numpy as np


def ent(frame):
    data = frame

    # Entropy of server data
    totalItems = 786384
    uniqueItems = 12
    divNumber = 65532

    print("Entropy")
    print((-((divNumber / totalItems) * math.log((divNumber / totalItems), 2))) * uniqueItems)

    # Set x and y values
    xValues = (data['Bytes Sent'])
    yValues = (data['Bytes Received'])

    # Calculate R and R squared of bytes sent and bytes received
    correlation_matrix = np.corrcoef(xValues, yValues)
    correlation_xy = correlation_matrix[0, 1]
    r = correlation_xy
    r_squared = correlation_xy ** 2
    print("\nR:")
    print(r)
    print("\nR squared:")
    print(r_squared)
