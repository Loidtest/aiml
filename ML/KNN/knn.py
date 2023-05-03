import pandas as pd

df = pd.read_csv('./WineQuality_Dataset.csv')
print(df.head(2))

X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol']]
y = df['quality']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(10)
knn.fit(X_train,y_train)
prediction = knn.predict(X_test)

from sklearn.metrics import classification_report
print("REPORT K=10 :\n\t",classification_report(prediction,y_test))
