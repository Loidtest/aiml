def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
        return header, data

header, data = read_csv('./WineQuality_Dataset.csv')
for row in data[:2]:
    print(row)

X = [[float(row[header.index(col)]) for col in ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol']] for row in data]
y = [int(row[header.index('quality')]) for row in data]

def train_test_split(X, y, test_size=0.3):
    test_len = int(len(X) * test_size)
    indices = list(range(len(X)))
    random.shuffle(indices)
    X_train = [X[i] for i in indices[test_len:]]
    X_test = [X[i] for i in indices[:test_len]]
    y_train = [y[i] for i in indices[test_len:]]
    y_test = [y[i] for i in indices[:test_len]]
    return X_train, X_test, y_train, y_test

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

def euclidean_distance(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

def k_nearest_neighbors(data, query_point, k):
    distances = []
    for index, point in enumerate(data):
        distance = euclidean_distance(point[:-1], query_point)
        distances.append((distance, index))
    distances.sort(key=lambda x: x[0])
    k_nearest = [data[distances[i][1]] for i in range(k)]
    return k_nearest

class KNeighborsClassifier:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            neighbors = k_nearest_neighbors(list(zip(self.X_train, self.y_train)), x + (None,), self.k)
            labels = [neighbor[-1] for neighbor in neighbors]
            prediction = max(set(labels), key=labels.count)
            predictions.append(prediction)
        return predictions

knn = KNeighborsClassifier(10)
knn.fit(X_train,y_train)
prediction = knn.predict(X_test)

def classification_report(y_pred, y_true):
    labels = sorted(set(y_true))
    report = {}
    for label in labels:
        tp = sum(1 for p,t in zip(y_pred,y_true) if p == label and t == label)
        fp = sum(1 for p,t in zip(y_pred,y_true) if p == label and t != label)
        fn = sum(1 for p,t in zip(y_pred,y_true) if p != label and t == label)
        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0
        f1_score = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0
        support = sum(1 for t in y_true if t == label)
        report[label] = {'precision': precision,
                         'recall': recall,
                         'f1-score': f1_score,
                         'support': support}
    return report

report_k10=classification_report(prediction,y_test)

print("REPORT K=10 :")
for key,value in report_k10.items():
   print("\t",key,value)