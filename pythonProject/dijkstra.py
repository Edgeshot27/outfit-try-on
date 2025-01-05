class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[[0 for col in range(v)] for row in range(v)]
    def mindist(self,dist,truth):
        mdist=float('inf')
        index=-1
        for i in range(self.v):
            if mdist>dist[i] and not truth[i]:
                mdist=dist[i]
                index=i
        return index
    def printed(self,src,dist):
        print(f'the distance of respective points from {src} is:')
        for i in range(self.v):
            print(f'{i}: {dist[i]}')
    def dijkstra(self,src):
        truth=[False]*self.v
        dist=[float('inf')]*self.v
        dist[src]=0
        for i in range(self.v):
            u=self.mindist(dist,truth)
            truth[u]=True
            for j in range(self.v):
                if self.graph[u][j]>0 and not truth[j] and dist[j]>dist[u] + self.graph[u][j]:
                    dist[j]=dist[u] + self.graph[u][j]
        self.printed(src,dist)
def adjacency(v):
    print('Enter elements fr the adjacency matrix:')
    mat=[]
    for i in range(v):
        row=list(map(int,input(f'row {i+1}:').split()))
        if len(row)!=v:
            print('invalid input')
            return
        mat.append(row)
    return mat
def main():
    v=int(input('Enter the number of vertices:'))
    g=Graph(v)
    g.graph=adjacency(v)
    src=int(input('enter the source :'))
    g.dijkstra(src)

if __name__=='__main__':
    main()