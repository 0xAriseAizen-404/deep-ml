def detect_cycles(ll_next, graph):
    # ll_next: list of next-node indices, -1 means null, start at node 0
    # graph: adjacency list of a directed graph
    # return (entry_index_or_-1, graph_has_cycle_bool)

    # Linked List Cycle Detection
    list_cycle_entry = -1
    if ll_next:
        visited = [False] * len(ll_next)
        ind = 0
        while ind != -1:
            if visited[ind]:
                list_cycle_entry = ind
                break
            visited[ind] = True
            ind = ll_next[ind]

    # Directed Graph Cycle Detection
    n = len(graph)
    visited = [False] * n
    in_stack = [False] * n
    def dfs(u):
        visited[u] = True
        in_stack[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs(v):
                    return True
            elif in_stack[v]:
                return True
        in_stack[u] = False
        return False

    graph_has_cycle = False
    for i in range(n):
        if not visited[i] and dfs(i):
            graph_has_cycle = True
            break
    return (list_cycle_entry, graph_has_cycle)