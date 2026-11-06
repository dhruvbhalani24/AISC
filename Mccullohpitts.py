def neuron(x, w, t):
    return 1 if sum(a*b for a, b in zip(x, w)) >= t else 0

def AND(a, b):
    return neuron([a, b], [1, 1], 2)

def OR(a, b):
    return neuron([a, b], [1, 1], 1)

def NOT(a):
    return neuron([a], [-1], 0)

def half_adder(a, b):
    s = a ^ b
    c = AND(a, b)
    return s, c

def full_adder(a, b, cin):
    s = a ^ b ^ cin
    c = (a & b) | (b & cin) | (a & cin)
    return s, c

print("A B | AND OR NOT(A) | HA(S,C) | FA(S,C)")
for a in range(2):
    for b in range(2):
        s, c = half_adder(a, b)
        print(a, b, "| ", AND(a,b), " ", OR(a,b), " ", NOT(a),
              "  | ", s, c, end=" | ")
        for cin in range(2):
            print(full_adder(a,b,cin), end=" ")
        print()