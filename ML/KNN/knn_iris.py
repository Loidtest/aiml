import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score

data = pd.read_csv('Iris.csv', index_col = 'Id')
data.head()

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
X = data[features]
y = data['Species']

x_train, x_test, y_train, y_test = tts(X, y, test_size=0.25, random_state = 1)

x_train.describe()

# KNN classifier
k = 5 # number of neighbors
model = KNeighborsClassifier(n_neighbors=k)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy_score(y_test, y_pred)