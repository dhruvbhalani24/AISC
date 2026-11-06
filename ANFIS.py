import numpy as np
from itertools import product

# 1. Create a small synthetic dataset
np.random.seed(1)
n = 300

temperature = np.random.uniform(15, 40, n)
humidity = np.random.uniform(20, 90, n)
occupancy = np.random.randint(0, 7, n)
appliances = np.random.uniform(0, 5, n)
hour = np.random.randint(0, 24, n)

# Energy consumption
Y = (0.03 * temperature + 0.008 * humidity +
     0.18 * occupancy + 0.45 * appliances +
     0.02 * hour + 0.5)

X = np.column_stack((temperature, humidity, occupancy,
                     appliances, hour))

# 2. Split training and testing data
X_train, X_test = X[:240], X[240:]
Y_train, Y_test = Y[:240], Y[240:]

# Normalize inputs using training data
mean = X_train.mean(axis=0)
std = X_train.std(axis=0) + 1e-8

X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# 3. Gaussian membership function
def gauss(x, c, s=1):
    return np.exp(-((x-c)**2) / (2*s**2))

# Two membership functions per input: Low and High
centers = [-0.7, 0.7]

# Generate 32 fuzzy rules
rules = list(product(centers, repeat=5))

# 4. Calculate firing strengths
def get_weights(X):
    firing = []

    for rule in rules:
        f = np.ones(len(X))

        for j in range(5):
            f *= gauss(X[:, j], rule[j])

        firing.append(f)

    firing = np.array(firing).T
    return firing / (firing.sum(axis=1, keepdims=True) + 1e-8)

# 5. Build ANFIS training matrix
def get_matrix(X):
    weights = get_weights(X)
    A = []

    for i in range(len(rules)): 
        A.append(weights[:, i:i+1] *
                  np.column_stack((X, np.ones(len(X)))))

    return np.hstack(A)

A = get_matrix(X_train)

# 6. Train consequent parameters using least squares
params = np.linalg.solve(
    A.T @ A + 0.001 * np.eye(A.shape[1]),
    A.T @ Y_train
)

# 7. Prediction
predicted = get_matrix(X_test) @ params

# 8. Evaluation
rmse = np.sqrt(np.mean((Y_test - predicted)**2))
mae = np.mean(np.abs(Y_test - predicted))

print("Actual:", np.round(Y_test[:5], 2))
print("Predicted:", np.round(predicted[:5], 2))
print("RMSE:", round(rmse, 3))
print("MAE:", round(mae, 3))