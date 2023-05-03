import numpy as np
import pandas as pd

def calculate_prob(x,mean,variance):
    exponent = np.exp(-((x-mean)**2/(2*variance)))
    return (1/(np.sqrt(2*np.pi)*variance))*exponent

data = pd.read_csv("iris.csv",index_col=0,na_values=['??','???','###'])
print(np.unique(data['SepalLengthCm']))
print(np.unique(data['SepalWidthCm']))
print(np.unique(data['PetalLengthCm']))
print(np.unique(data['PetalWidthCm']))
print(np.unique(data['Species'])) 

data['Species'].replace('Iris-setosa',1,inplace=True)
data['Species'].replace('Iris-versicolor',2,inplace=True)
data['Species'].replace('Iris-virginica',3,inplace=True)
data['Species']=data['Species'].astype('int64')

data['SepalLengthCm'].fillna(data['SepalLengthCm'].mean(),inplace=True)
data['SepalWidthCm'].fillna(data['SepalWidthCm'].mean(),inplace=True)
data['PetalLengthCm'].fillna(data['PetalLengthCm'].mean(),inplace=True)

class_label = np.array(['Iris-setosa' 'Iris-versicolor' 'Iris-virginica'])
features = np.array(['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])

AM = np.zeros((len(features),len(class_label)))
AV = np.zeros((len(features),len(class_label)))

for i in range(len(class_label)):
    clas = pd.DataFrame(data[data['Species'].isin([i+1])])
    for j in range(len(features)):
        AM[j][i] = np.mean(clas[features[j]])
        AV[j][i] = np.var(clas[features[j]])

print("Enter inputs:")
SL = float(input("Enter the SepalLength: "))
SW = float(input("Enter the SepalWidth: "))
PL = float(input("Enter the PetalLength: "))
PW = float(input("Enter the PetalWidth: "))
x = [SL,SW,PL,PW]
A = np.zeros((len(features),len(class_label)))

for i in range(len(features)):
    A[i] = calculate_prob(x[i],AM[i],AV[i])
print(A)

large = 0.0
pc = np.array([0.33,0.33,0.33])
for i in range(len(class_label)):
    for j in range(len(features)):
        pc[i] = pc[i]*A[j][i]
        if large < pc[i]:
            large = pc[i]
            k = i
        print(pc)
print(class_label[k])
