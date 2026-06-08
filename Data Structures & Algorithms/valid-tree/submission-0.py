class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(0)

        return len(visited) == n