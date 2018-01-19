from collections import deque

print('Importing graph search module')


def dfs(graph, start):
    """
    Search through all paths in graph down each branch before any of its neighbors.
    Runtime: O(V + E)
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, next, goal, path + [next])


def bfs(graph, start):
    """
    Search through all paths in graph by looking through each vertice's neighbors.
    Runtime: O(V + E)
    """
    visited, queue = set(), deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":
    graph = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }

    print(dfs(graph, 'A'))  # {'E', 'D', 'F', 'A', 'C', 'B'}
    print(dfs_recursive(graph, 'C'))  # {'E', 'D', 'F', 'A', 'C', 'B'}
    print(list(dfs_paths(graph, 'A', 'F')))  # [['A','C', 'F'], ['A, 'B', 'E', 'F']]
    print(list(dfs_paths_recursive(graph, 'C', 'F')))  # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
    print(bfs(graph, 'A'))  # {'B', 'C', 'A', 'F', 'D', 'E'}
    print(list(bfs_paths(graph, 'A', 'F')))  # [['A','C', 'F'], ['A, 'B', 'E', 'F']]
    print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']
