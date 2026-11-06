def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:
        pq.sort()
        f, g, node, path = pq.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for nxt, cost in graph[node]:
                if nxt not in visited:
                    ng = g + cost
                    pq.append((ng + h[nxt], ng, nxt, path + [nxt]))

    print("No path found")


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('E', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'G': []
}

h = {'A': 4, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'G': 0}

astar(graph, h, 'A', 'G')