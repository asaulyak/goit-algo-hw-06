def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex].items():
            distance = distances[current_vertex] + neighbor[1]['weight']

            if distance < distances[neighbor[0]]:
                distances[neighbor[0]] = distance

        unvisited.remove(current_vertex)

    return distances

