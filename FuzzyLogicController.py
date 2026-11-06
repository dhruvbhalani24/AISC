import numpy as np

# Membership functions
def trimf(x, a, b, c):
    return max(0, min((x-a)/(b-a+1e-9), (c-x)/(c-b+1e-9)))

def trapmf(x, a, b, c, d):
    return max(0, min((x-a)/(b-a+1e-9), 1, (d-x)/(d-c+1e-9)))

# Input values
d = 35       # Traffic density
w = 100      # Waiting time

# Fuzzification
dl = trapmf(d, 0, 0, 10, 15)
dm = trimf(d, 10, 20, 30)
dh = trapmf(d, 25, 35, 50, 50)

ws = trapmf(w, 0, 0, 20, 30)
wm = trimf(w, 20, 50, 80)
wl = trapmf(w, 70, 90, 120, 120)

# Rule strengths (AND = minimum)
r1 = min(dl, ws)  # Low density + Short wait
r2 = min(dm, wm)  # Medium density + Moderate wait
r3 = min(dh, wl)  # High density + Long wait
r4 = min(dh, ws)  # High density + Short wait
r5 = min(dl, wl)  # Low density + Long wait

# Output membership functions
x = np.arange(10, 91, 1)

short = np.array([trimf(i, 10, 20, 30) for i in x])
medium = np.array([trimf(i, 30, 45, 60) for i in x])
long = np.array([trimf(i, 60, 75, 90) for i in x])

# Apply rules (clipping)
out1 = np.minimum(r1, short)
out2 = np.minimum(r2, medium)
out3 = np.minimum(r3, long)
out4 = np.minimum(r4, medium)
out5 = np.minimum(r5, medium)

# Aggregation (maximum)
final = np.maximum.reduce([out1, out2, out3, out4, out5])

# Defuzzification (Centroid method)
result = np.sum(x * final) / (np.sum(final) + 1e-9)

print("Green duration:", round(result, 2), "seconds")