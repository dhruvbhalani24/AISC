import numpy as np

# English and Hindi words represented using bipolar binary codes
# -1 and +1 are used instead of 0 and 1

english = np.array([
    [ 1,  1,  1, -1, -1, -1],  # Dog
    [ 1, -1, -1,  1,  1, -1],  # Cat
    [-1,  1, -1,  1, -1,  1]   # Sun
])

hindi = np.array([
    [ 1,  1, -1, -1,  1, -1],  # कुत्ता
    [ 1, -1,  1, -1, -1,  1],  # बिल्ली
    [-1,  1,  1,  1, -1, -1]   # सूरज
])

# Hebbian learning
W = english.T @ hindi

# Forward recall: English -> Hindi
def forward(x):
    return np.where(x @ W >= 0, 1, -1)

# Reverse recall: Hindi -> English
def reverse(y):
    return np.where(y @ W.T >= 0, 1, -1)

# Test
for i in range(len(english)):
    y = forward(english[i])
    x = reverse(hindi[i])

    print("--- Forward test (English -> Hindi) ---")
    print("Input English   :", english[i])
    print("Recalled Hindi  :", y)
    print("Expected Hindi  :", hindi[i])

    print("--- Reverse test (Hindi -> English) ---")
    print("Input Hindi     :", hindi[i])
    print("Recalled English:", x)
    print("Expected English:", english[i])
    print()