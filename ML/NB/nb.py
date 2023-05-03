import pandas as pd
import seaborn as sns

df = pd.read_csv('./Glass_Dataset.csv')
print(df.head(2))

X = df.drop(columns=['Type'])
y = df['Type']

sns.countplot(df['Type'], color='blue')

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_train,y_train)

prediction = nb.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(prediction,y_test))
