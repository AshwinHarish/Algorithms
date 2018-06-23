# Dijkstra's
graph = {
    1:{ 2:10, 5:100},
    2:{ 1:10, 3:50},
    3:{ 2:50, 4:20, 5:10},
    4:{ 3:20, 5:60},
    5:{ 1:100, 3:10, 4:600}
}
def Dijkstras (graph,s):
    d, visited = [float('inf')]*len(graph),[0]*len(graph)
    nodes = graph.keys()
    d[s-1] = 0
    vertices = [s]
    visited [s-1] = 1
    nodes.remove(s)
    while len(vertices) != len(graph):
        edges = {}
        for u in vertices:
            for v in graph[u].keys():
                if visited [v-1] == 0:
                    t = d[u-1] + graph[u][v]
                    edges.update({t:[u,v]})
        min_d = min(edges.keys())
        e = edges[min_d]
        d[e[1]-1] = min_d
        nodes.remove(e[1])
        vertices.append(e[1])
        visited[e[1]-1] = 1
    for i in range(len(graph)):
        print (i+1),' : ',d[i]
Dijkstras (graph,3)
