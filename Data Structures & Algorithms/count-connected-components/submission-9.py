class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conn_comp = n
        par = [i for i in range(n)]

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        for edge1, edge2 in edges:
            root1, root2 = find(edge1), find(edge2)
            if root1 == root2:
                continue
            par[root2] = root1
            conn_comp -= 1
        
        return conn_comp