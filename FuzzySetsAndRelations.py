import numpy as np

# AQI levels: Good, Moderate, Poor, Severe
A = np.array([1.0, 0.6, 0.2, 0.0])

# Health effects: Healthy, Mild, Serious
B = np.array([0.9, 0.5, 0.1])

# Desired health condition
C = np.array([1.0, 0.6, 0.2])

# Fuzzy operations
print("Union:", np.maximum(A, A))
print("Intersection:", np.minimum(A, A))
print("Bounded sum:", np.minimum(A + A, 1))
print("Bounded difference:", np.maximum(A - A, 0))

# Cartesian product: AQI levels x health effects
R = np.minimum.outer(A, B)
print("\nCartesian relation:\n", R)

# Max-min composition: AQI set A with relation R
result = np.max(np.minimum(A[:, None], R), axis=0)
print("\nMax-min composition:", result)

# Max-product composition
result_product = np.max(A[:, None] * R, axis=0)
print("Max-product composition:", result_product)