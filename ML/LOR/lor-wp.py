def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
        return header, data

header, data = read_csv('./Titanic_Dataset.csv')

sex = [[1 if row[header.index('Sex')] == 'male' else 0] for row in data]
header.append('male')
data = [row + s for row,s in zip(data,sex)]
data = [row for row in data if all(x != '' for x in row)]
header = ['Pclass', 'male', 'Age', 'SibSp', 'Parch', 'Survived']
data = [[row[header.index(col)] for col in header] for row in data]

for row in data[:5]:
    print(row)

X = [[int(row[header.index(col)]) for col in ['Pclass', 'male', 'Age', 'SibSp', 'Parch']] for row in data]
y = [int(row[header.index('Survived')]) for row in data]

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

class LogisticRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def cost(self, X, y):
        m = len(y)
        h = [self.sigmoid(sum(self.coef_[j] * x[j] for j in range(len(x))) + self.intercept_) for x in X]
        return (-1/m) * sum(y[i] * math.log(h[i]) + (1 - y[i]) * math.log(1 - h[i]) for i in range(m))

    def fit(self, X_train, y_train, alpha=0.1, num_iter=10000):
        self.coef_ = [0] * len(X_train[0])
        self.intercept_ = 0
        m = len(y_train)
        for _ in range(num_iter):
            h = [self.sigmoid(sum(self.coef_[j] * x[j] for j in range(len(x))) + self.intercept_) for x in X_train]
            self.coef_ = [self.coef_[j] - (alpha/m) * sum((h[i] - y_train[i]) * X_train[i][j] for i in range(m)) for j in range(len(self.coef_))]
            self.intercept_ -= (alpha/m) * sum(h[i] - y_train[i] for i in range(m))

    def predict(self, X_test):
        return [round(self.sigmoid(sum(self.coef_[j] * x[j] for j in range(len(x))) + self.intercept_)) for x in X_test]

lgr = LogisticRegression()
lgr.fit(X_train,y_train)

prediction = lgr.predict(X_test)

def classification_report(y_true, y_pred):
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
        report