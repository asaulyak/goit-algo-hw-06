def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            return dfs(graph, neighbor, visited)

    return visited