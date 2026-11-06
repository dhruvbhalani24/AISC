import random
import math

X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 1, 1, 0]

H = 4
lr = 0.5

w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(H)]
b1 = [0] * H
w2 = [random.uniform(-1, 1) for _ in range(H)]
b2 = 0

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def forward(x):
    h = [sigmoid(w1[j][0]*x[0] + w1[j][1]*x[1] + b1[j]) for j in range(H)]
    out = sigmoid(sum(w2[j]*h[j] for j in range(H)) + b2)
    return h, out

for _ in range(20000):
    for x, t in zip(X, y):
        h, out = forward(x)
        d2 = (t - out) * out * (1 - out)

        for j in range(H):
            d1 = d2 * w2[j] * h[j] * (1 - h[j])
            w2[j] += lr * d2 * h[j]
            w1[j][0] += lr * d1 * x[0]
            w1[j][1] += lr * d1 * x[1]
            b1[j] += lr * d1

        b2 += lr * d2   

print("XOR:", [int(forward(x)[1] >= 0.5) for x in X])