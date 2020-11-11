# With this, we will build a decision tree and display the results using sklearn

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from six import StringIO
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from IPython.display import Image as im
import pydotplus
from PIL import Image

# set column names for the dataset
col_names = ['Source Port', 'Destination Port', 'NAT Source Port', 'NAT Destination Port', 'Action', 'Bytes', 'Bytes Sent',
             'Bytes Received', 'Packets', 'Elapsed Time (sec)', 'pkts_sent', 'pkts_received' ]

# Import the dataset as a CSV and set it as a Dataframe
port_DATA = pd.read_csv("finalData.csv", header=0, names=col_names)

# Some of the values are reading as infinite. Replace with NaN
port_DATA.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop the Rows with NaN values
port_DATA.dropna(inplace=True)

# instantiate encoder
lb = LabelEncoder()

# make a copy of the dataset
port_DATA_copy = port_DATA.copy()

# set up a list to replace the action categorical values with numerical ones
replace_list = {'Action': {'allow': 0, 'deny': 1, 'drop': 2, 'reset-both': 3}}

# replace the values
port_DATA_copy.replace(replace_list, inplace=True)

# Select our Independent Features
feature = ['Source Port', 'Destination Port', 'NAT Source Port', 'NAT Destination Port', 'Bytes',
           'Bytes Sent', 'Bytes Received']

# Set x values to the independent features
X = port_DATA_copy[feature]

# set y values to the target feature
Y = port_DATA_copy['Action']

# set up our test and train values with sklearn. Test size will be 30% of the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Set up our Decision Tree Classifier
tree = DecisionTreeClassifier(criterion="entropy", max_depth=6)

# Fit our training data to the classifier
tree = tree.fit(X_train, Y_train)

# use the prediction function to make a prediction based on the x test set
predict = tree.predict(X_test)

# use the y test set with the predictions based off of the x test set to find an accuracy percentage
print("Accuracy of Test Model: ", metrics.accuracy_score(Y_test, predict))

# now we will display the decision tree
# create a memory file with stringIO
display_data = StringIO()

# create a graphic representation of the decision tree for the dataset. we will use display_data to create
# output file. This will be a dot file
export_graphviz(tree, out_file=display_data, filled=True, rounded=True, special_characters=True,
                feature_names=feature)

# convert the dot file over to a graph
graph = pydotplus.graph_from_dot_data(display_data.getvalue())

# write png to file name
graph.write_png('ports.png')

# render the decision tree. It will be a .png
im(graph.create_png())

# open the image file for the decision tree
img = Image.open('ports.png')

# display the graph
img.show()
