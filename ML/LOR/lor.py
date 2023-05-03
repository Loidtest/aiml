import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./Titanic_Dataset.csv')

sns.countplot(x='Survived',data=df,hue='Sex')
plt.show()
sns.countplot(x='Survived',data=df,hue='Pclass')
plt.show()

sex = pd.get_dummies(df['Sex'],drop_first=True)
df = pd.concat([df,sex],axis=1)
df.drop(['PassengerId','Name','Cabin', 'Embarked','Fare','Ticket','Sex'],axis=1,inplace=True)
df.dropna(inplace=True)
print(df.head(5))

X = df[['Pclass','male','Age','SibSp','Parch']]
y = df['Survived']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression()
lgr.fit(X_train,y_train)

prediction = lgr.predict(X_test)

from sklearn.metrics import classification_report
print("\n\nREPORT :\n\t",classification_report(y_test,prediction))
