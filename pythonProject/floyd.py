def floyd(graph):
    v=len(graph)
    dist=[row[:] for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    print(dist)

def main():
    v=int(input('enter number of vertices:'))
    print('Enter the data in the for starting index, ending vertex and weight,type done when all data added.')
    graph=[[float('inf')] * v for _ in range(v)]
    for i in range(v):
        graph[i][i]=0
    while True:
        data=input()
        if data.lower()=='done':
            break
        try:
            start,end,weight=map(int,data.split())
            graph[start][end]=weight
        except ValueError:
            print('Invalid input')

    floyd(graph)

if __name__ == '__main__':
    main()
