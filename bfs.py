def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return visited

    vertex = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)

    return bfs(graph, queue, visited)
