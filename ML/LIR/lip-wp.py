def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
        return header, data

header, data = read_csv('./StudentScore_Dataset.csv')
for row in data:
    print(row)

X = [[float(row[header.index('Hours')])] for row in data]
y = [float(row[header.index('Scores')]) for row in data]

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

class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X_train, y_train):
        x_mean = sum(x[0] for x in X_train) / len(X_train)
        y_mean = sum(y_train) / len(y_train)
        numerator = sum((x[0] - x_mean) * (y - y_mean) for x, y in zip(X_train, y_train))
        denominator = sum((x[0] - x_mean) ** 2 for x in X_train)
        self.coef_ = numerator / denominator
        self.intercept_ = y_mean - self.coef_ * x_mean

    def predict(self, X_test):
        return [self.coef_ * x[0] + self.intercept_ for x in X_test]

lr = LinearRegression()
lr.fit(X_train,y_train)

prediction = lr.predict(X_test)

def mean_absolute_error(y_true, y_pred):
    return sum(abs(t - p) for t,p in zip(y_true,y_pred)) / len(y_true)

def mean_squared_error(y_true, y_pred):
    return sum((t - p) ** 2 for t,p in zip(y_true,y_pred)) / len(y_true)

print("MEA : ",mean_absolute_error(y_test, prediction))
print("MSE : ",mean_squared_error(y_test, prediction))