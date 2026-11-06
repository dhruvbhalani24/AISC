from collections import deque

def next_states(x, y):
    return [
        (4, y), (x, 3), (0, y), (x, 0),
        (x-min(x, 3-y), y+min(x, 3-y)),
        (x+min(y, 4-x), y-min(y, 4-x))
    ]

def solve(method):
    start = (0, 0)
    q = deque([start])
    visited = {start}
    parent = {start: None}

    while q:
        s = q.popleft() if method == "BFS" else q.pop()
        x, y = s

        if x == 2 or y == 2:
            path = []
            while s is not None:
                path.append(s)
                s = parent[s]
            return path[::-1]

        for ns in next_states(x, y):
            if ns not in visited:
                visited.add(ns)
                parent[ns] = s
                q.append(ns)

print("BFS:", solve("BFS"))
print("DFS:", solve("DFS"))