import numpy as np
import pandas as pd
data=pd.read_csv("/home/user/Downloads/iris.csv", index_col=0, na_values=(["??", "????", "###"]))
data["Species"].replace('Iris-setosa', 1, inplace=True)
data["Species"].replace('Iris-versicolor', 2, inplace=True)
data["Species"].replace('Iris-virginica', 3, inplace=True)
data["Species"]=data["Species"].astype("int64")
class_label=np.array(['Iris-sentosa', 'Iris-versicolor', 'Iris-virginica'])
data['SepalLengthCm'].fillna(data['SepalLengthCm'].mean(), inplace=True)
data['SepalWidthCm'].fillna(data['SepalWidthCm'].mean(), inplace=True)
data['PetalLengthCm'].fillna(data['PetalLengthCm'].mean(), inplace=True)
data['PetalWidthCm'].fillna(data['PetalWidthCm'].mean(), inplace=True)
features=np.array(['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
data['Distance']=0
print("Enter the input: ")
SL=float(input("Enter the sepal length: "))
SW=float(input("Enter the sepal width: "))
PL=float(input("Enter the petal length: "))
PW=float(input("Enter the petal width: "))
k=75
sample=[SL, SW, PL, PW]
for i in range (len(data)):
    for j in range (len(features)):
        data.iloc[i, 5]+=((sample[j]-data.iloc[i, j])**2)
sorted_data=data.sort_values(by='Distance')
output=sorted_data.iloc[0:k, 4]
Y=output.value_counts().index[0]
print("The sample {} belongs to the class {}".format(sample, class_label[Y-1]))
