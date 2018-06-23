# DFS
graph={
        1:[2,3],
        2:[1,3,4,5],
        3:[1,2,6,7],
        4:[2,5,8,9],
        5:[2,4,9],
        6:[3,7],
        7:[3,6],
        8:[4,9],
        9:[4,5,8,10],
        10:[9]
}
visited=[0]*10
def dfs(node):
        visited[node-1]=1
        print node
        for k in graph[node]:
                if visited[k-1]==0:
                        dfs(k)
dfs(1)
