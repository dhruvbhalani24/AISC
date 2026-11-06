from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and \
           (m == 0 or m >= c) and \
           (3-m == 0 or 3-m >= 3-c)

def solve():
    start, goal = (3, 3, 0), (0, 0, 1)
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()
        if state == goal:
            return path + [state]

        m, c, b = state
        for x, y in [(1,0), (2,0), (0,1), (0,2), (1,1)]:
            s = (m-x, c-y, 1) if b == 0 else (m+x, c+y, 0)

            if valid(s[0], s[1]) and s not in visited:
                visited.add(s)
                q.append((s, path + [state]))

print("BFS:", solve())