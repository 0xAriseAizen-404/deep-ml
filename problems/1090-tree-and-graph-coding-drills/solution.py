def tree_and_graph_drills(task, *args):
    # task is one of: "lca", "clone", "min_removals", "word_break"
    if task == "lca":
        tree, root, p, q = args
        def lca(node):
            if node is None or node == p or node == q:
                return node
            left = lca(tree[node][0])
            right = lca(tree[node][1])
            if left and right:
                return node
            return left if left else right
        return lca(root)
        
    if task == "clone":
        graph = args[0]
        clone = {}
        for node, neighbors in graph.items():
            clone[node] = sorted(neighbors)
        return dict(sorted(clone.items()))
        
    if task == "min_removals":
        parentheses = args[0]
        open_cnt = 0
        removals = 0
        for ch in parentheses:
            if ch == '(':
                open_cnt += 1
            else:
                if open_cnt:
                    open_cnt -= 1
                else:
                    removals += 1
        return removals + open_cnt
    
    if task == "word_break":
        s, words = args
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in words:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)
        