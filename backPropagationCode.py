import numpy as np

X = np.array([[1,40],[2,50],[3,55],[4,65],[5,70],[6,80],[7,85],[8,90]]) / [8, 100]
Y = np.array([0,0,0,1,1,1,1,1]).reshape(-1, 1)

np.random.seed(1)
W1, b1 = np.random.rand(2, 3), np.zeros(3)
W2, b2 = np.random.rand(3, 1), 0.0
lr = 0.5

sigmoid = lambda x: 1 / (1 + np.exp(-x))

for _ in range(5000):
    h = sigmoid(X @ W1 + b1)
    o = sigmoid(h @ W2 + b2)

    do = o - Y
    dh = (do @ W2.T) * h * (1 - h)

    W2 -= lr * h.T @ do / len(X)
    b2 -= lr * do.mean()
    W1 -= lr * X.T @ dh / len(X)
    b1 -= lr * dh.mean(axis=0)

o = sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2)
print("Predicted Output:")
for p in o.ravel():
    print(round(p, 2), "Pass" if p >= 0.5 else "Fail")