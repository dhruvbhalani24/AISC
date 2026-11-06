def h(s):
    return sum(abs(i//3 - (x-1)//3) + abs(i%3 - (x-1)%3)
               for i, x in enumerate(s) if x)

def solve(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    pq = [(h(start), 0, start, [])]
    visited = set()

    while pq:
        pq.sort()
        f, g, s, path = pq.pop(0)

        if s == goal:
            for p in path + [s]:
                print(p[:3], p[3:6], p[6:])
            print("Moves:", g)
            return

        if s in visited:
            continue
        visited.add(s)

        i = s.index(0)

        for j in [i-3, i+3, i-1, i+1]:
            if 0 <= j < 9 and (abs(i//3-j//3) + abs(i%3-j%3) == 1):
                t = list(s)
                t[i], t[j] = t[j], t[i]
                t = tuple(t)

                if t not in visited:
                    pq.append((g+1+h(t), g+1, t, path+[s]))

    print("No solution")


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solve(start)