import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./StudentScore_Dataset.csv')
print(df)

X = df[['Hours']]
y = df['Scores']

plt.scatter(df['Hours'], df['Scores'])
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)

prediction = lr.predict(X_test)

from sklearn import metrics
print("MEA : ",metrics.mean_absolute_error(y_test, prediction))
print("MSE : ",metrics.mean_squared_error(y_test, prediction))
