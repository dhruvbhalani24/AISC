import numpy as np
import csv

with open("som_lvq_dataset.csv") as f:
    data = list(csv.reader(f))[1:]

X = np.array([[float(row[0]), float(row[1])]
              for row in data])
Y = np.array([int(row[2]) for row in data])

# Initialize prototypes
W = X[[0, 4, 8]].copy()
labels = np.array([0, 1, 2])

lr = 0.1

for epoch in range(100):
    for x, y in zip(X, Y):
        winner = np.argmin(np.linalg.norm(W - x, axis=1))

        if labels[winner] == y:
            W[winner] += lr * (x - W[winner])
        else:
            W[winner] -= lr * (x - W[winner])

print("LVQ Prototypes:")
print(W)
print("Labels:")
print(labels)