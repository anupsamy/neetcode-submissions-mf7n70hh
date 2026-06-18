class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]  # path compression
                x = par[x]
            return x

        conn_comp = n
        for edge1, edge2 in edges:
            root1, root2 = find(edge1), find(edge2)
            if root1 == root2:
                continue
            par[root2] = root1  # union the roots, not the nodes
            conn_comp -= 1

        return conn_comp