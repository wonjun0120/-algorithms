def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
