# Prims
graph = {
        1 : { 2:10, 5:100 },
        2 : { 1:10, 3:50 },
        3 : { 2:50, 4:20, 5:10 },
        4 : { 3:20, 5:60 },
        5 : { 1:100, 3:10, 4:60 }
}
def Prims(graph):
    U,V = set([1]),set(graph.keys())
    visited = [0]*len(graph)
    edges = []
    cost = 0
    while U != V:
        e = {}
        for u in U:
            for v in (V-U):
                if visited[v-1] == 0 and v in graph[u].keys():
                    e.update({graph[u][v]:[u,v]})
        mincost = min(e.keys())
        edge = e[mincost]
        edge += [mincost]
        cost += mincost
        edges.append(edge)
        U = U|set(edge)
        visited[edge[0]-1],visited[edge[1]-1] = 1,1
    return cost,edges

cost,edges = Prims(graph)
print "Cost : ",cost
print "Edges:"
for i in edges:
        print i[2],' : ',i[0],' and ',i[1]

