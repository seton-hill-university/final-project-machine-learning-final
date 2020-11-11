# importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df= pd.read_csv ('finalData.csv')


# I used two different dimentionality reduction.
# The below one is Random Forest
# It works with only numeric values
# This method shows you what feature are more important than the other
# And you select features based on their weight
from sklearn.ensemble import RandomForestRegressor

# Dropping action column because it's not numeric variable
df=df.drop(['Action'], axis=1)
model = RandomForestRegressor(random_state=1, max_depth=10)
df=pd.get_dummies(df)
model.fit(df,df.Bytes)

features = df.columns
importances = model.feature_importances_
indices = np.argsort(importances)[-9:]  # top 10 features
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

from sklearn.feature_selection import SelectFromModel
feature = SelectFromModel(model)
Fit = feature.fit_transform(df, df.Bytes)
print(Fit)

#After using this graph shows that NAT source port column is the least important.


##########################
#This is Low Variance Filter method that shows you what features that can be removed and don't impact our dataset a lot.

n = df.isnull().sum()/len(df)*100
print(n)

#calculating variance of all numeric variables.
m = df.var()

num = df.var()
print(num)

# Due to Variance values of sttributes, I will drop all atributes less than 2 because they have low variance to my dataset.
#looking on how many columns I have before dropping some of them.
print(len(df.columns))
df= df.drop(['Bytes Sent','pkts_sent'], axis=1)
#Counting columns and see if I was able to drop targeted columns
print(len(df.columns))

print(len(df))





