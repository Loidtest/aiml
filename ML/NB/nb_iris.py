import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
data = pd.read_csv('iris.csv', index_col = 'Id')
data.head()
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
X = data[features]
y = data['Species']
x_train, x_test, y_train, y_test = tts(X, y, test_size=0.25, random_state = 1)
x_train.describe()
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy_score(y_test, y_pred)