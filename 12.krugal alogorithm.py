class Kruskal:
    def find(parent,i):
        if(parent[i]==i):
            return i
        return Kruskal.find(parent, parent[i])
    def union(parent, rank, x, y):
        xroot = Kruskal.find(parent, x)
        yroot = Kruskal.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def MST(graph):
        edges = []
        for i in range(len(graph)):
            for j in range(i,len(graph[i])):
                if (graph[i][j]!=0 and graph[i][j]!=-1):
                    edges.append((i,j,graph[i][j]))
        edges = sorted(edges, key=lambda item:item[2])
        V = len(graph)
        result = []
        i = 0
        e = 0
        parent = []
        rank = []
        for node in range(V):
            parent.append(node)
            rank.append(0)
        while e < V - 1:
            u, v, w = edges[i]
            i = i + 1
            x = Kruskal.find(parent, u)
            y = Kruskal.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                Kruskal.union(parent, rank, x, y)
        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
if __name__ == "__main__":
    graph = [
    [ 0, 4, -1, -1, -1, -1, -1, 8, -1],
    [ 4, 0, 8, -1, -1, -1, -1, 11, -1],
    [-1, 8, 0, 7, -1, 4, -1, -1, 2],
    [-1, -1, 7, 0, 9, 14, -1, -1, -1],
    [-1, -1, -1, 9, 0, 10, -1, -1, -1],
    [-1, -1, 4, 14, 10, 0, 2, -1, -1],
    [-1, -1, -1, -1, -1, 2, 0, 1, 6],
    [ 8, 11, -1, -1, -1, -1, 1, 0, 7],
    [-1, -1, 2, -1, -1, -1, 6, 7, 0]
    ]
    Kruskal.MST(graph)
