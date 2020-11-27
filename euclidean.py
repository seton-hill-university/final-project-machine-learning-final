# Euclidean Dist

import pandas as pd
import numpy as np

def euc (frame):

    # splits the df in half by rows
    df1 = df.iloc[:, :65533]
    df2 = df.iloc[:, 65533:]

    columns = ["Bytes", "Bytes Sent"]
    # compares each col of df1 to the corresponding col of df2
    def Euclidean_Dist(df1, df2, cols=['Bytes', 'Bytes Sent']):
        return np.linalg.norm(df1[cols].values - df2[cols].values,
                              axis=1)

    print(Euclidean_Dist(df1, df2))


    # EXAMPLE DATAFRAME THAT WORKS
    # df1 = pd.DataFrame({'user_id':[214,214,214],
    #                 'x_coord':[-55.2,-55.2,-55.2],
    #                 'y_coord':[22.1,22.1,22.1]})

    # df2 = pd.DataFrame({'user_id':[512, 362, 989],
    #                     'x_coord':[-15.2, 65.1, -84.8],
    #                     'y_coord':[19.1, 71.4, 13.7]})


    # def Euclidean_Dist(df1, df2, cols=['x_coord','y_coord']):
    #     return np.linalg.norm(df1[cols].values - df2[cols].values,
    #                    axis=1)

    # Euclidean_Dist(df1, df2)