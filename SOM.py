import numpy as np
import csv

with open("som_lvq_dataset.csv") as f:
    data = list(csv.reader(f))[1:]

np.random.seed(1)

X = np.array([[float(row[0]), float(row[1])] for row in data])

# 2x2 SOM grid, each neuron has a 2D weight vector
W = np.random.rand(2, 2, 2)
lr = 0.5

for _ in range(100):
    for x in X:
        dist = np.linalg.norm(W - x, axis=2)
        bmu = np.unravel_index(np.argmin(dist), (2, 2))

        for i in range(2):
            for j in range(2):
                # neighbours = grid cells within Manhattan distance 1 of the BMU
                if abs(bmu[0] - i) + abs(bmu[1] - j) <= 1:
                    W[i, j] += lr * (x - W[i, j])
    lr *= 0.99

print("SOM weights:")
print(W.reshape(4, 2))

# Map patients to winning neurons
clusters = []
for x in X:
    dist = np.linalg.norm(W - x, axis=2)
    bmu = np.unravel_index(np.argmin(dist), (2, 2))
    clusters.append(bmu[0] * 2 + bmu[1])

clusters = np.array(clusters)

for i, c in enumerate(clusters):
    print("Patient", i + 1, "-> Cluster", c)