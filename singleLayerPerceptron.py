def perceptron(X, y):
    w = [0] * len(X[0])
    b = 0

    for _ in range(100):
        for i in range(len(X)):
            out = int(sum(w[j]*X[i][j] for j in range(len(w))) + b > 0)
            error = y[i] - out

            for j in range(len(w)):
                w[j] += error * X[i][j]
            b += error

    return [int(sum(w[j]*x[j] for j in range(len(w))) + b > 0) for x in X]


X = [[0,0], [0,1], [1,0], [1,1]]

print("AND:", perceptron(X, [0,0,0,1]))
print("OR:", perceptron(X, [0,1,1,1]))
print("NOT:", perceptron([[0], [1]], [1,0]))