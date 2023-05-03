def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
        return header, data

header, data = read_csv('./Glass_Dataset.csv')
for row in data[:2]:
    print(row)

X = [[float(row[header.index(col)]) for col in header if col != 'Type'] for row in data]
y = [int(row[header.index('Type')]) for row in data]

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

class GaussianNB:
    def __init__(self):
        self.priors = None
        self.means = None
        self.stds = None

    def fit(self, X_train, y_train):
        labels = sorted(set(y_train))
        self.priors = [sum(1 for y in y_train if y == label) / len(y_train) for label in labels]
        self.means = [[sum(x[j] for x,y in zip(X_train,y_train) if y == label) / sum(1 for y in y_train if y == label) for j in range(len(X_train[0]))] for label in labels]
        self.stds = [[(sum((x[j] - self.means[i][j]) ** 2 for x,y in zip(X_train,y_train) if y == label) / sum(1 for y in y_train if y == label)) ** 0.5 for j in range(len(X_train[0]))] for i,label in enumerate(labels)]

    def predict(self, X_test):
        def normal_pdf(x, mean, std):
            return (1 / (std * (2 * math.pi) ** 0.5)) * math.exp(-0.5 * ((x - mean) / std) ** 2)

        def posterior(x, label_index):
            return self.priors[label_index] * product(normal_pdf(x[j], self.means[label_index][j], self.stds[label_index][j]) for j in range(len(x)))

        return [max(range(len(self.priors)), key=lambda i: posterior(x,i)) + 1 for x in X_test]

nb = GaussianNB()
nb.fit(X_train,y_train)

prediction = nb.predict(X_test)

def accuracy_score(y_true, y_pred):
    return sum(1 for t,p in zip(y_true,y_pred) if t == p) / len(y_true)

print(accuracy_score(y_test,prediction))
