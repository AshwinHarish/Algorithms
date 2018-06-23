# BFS
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
visited = [0]*10
queue = []
def bfs(source):
        visited[source-1] = 1
        queue.append(source)
        while(queue):
                print queue[0]
                vertex = queue.pop(0)
                for node in graph[vertex]:
                        if visited[node-1] == 0:
                                queue.append(node)
                                visited[node-1] = 1
bfs(1)
