def mul(x,y):
    if x<10 or y<10 :
        return x*y
    n=max(len(str(x)),len(str(y)))
    m=n//2
    power=10**m
    x1=x//power
    x2=x%power
    y1=y//power
    y2=y%power
    a=mul(x1,y1)
    b=mul(x2,y2)
    c=mul((x1+x2),(y1+y2))-a-b
    return a*(10**(2*m))+c*(10**(m))+b
x=int(input())
y=int(input())
print(mul(x,y))


class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def max_dead(jobs):
    mdeadline = float('-inf')
    for job in jobs:
        mdeadline = max(mdeadline, job.deadline)
    return mdeadline


def sorted_jobs(jobs):
    return sorted(jobs, key=lambda x: x.profit, reverse=True)


def operation(jobs):
    total = 0
    m = max_dead(jobs)
    slot = [-1] * (m)
    for job in jobs:
        for j in range(job.deadline - 1, -1, -1):
            if slot[j] == -1:
                slot[j] = job.id
                total += job.profit
                break
    return total, slot


def main():
    jobs = []
    n = int(input("Enter the number of jobs: "))
    for i in range(n):
        print('For job:', i + 1)
        id = int(input('Enter the job id:'))
        deadline = int(input('enter the deadline:'))
        profit = int(input('enter the profit:'))
        jobs.append(Job(id, deadline, profit))
    jobs = sorted_jobs(jobs)
    mdeadline = max_dead(jobs)
    total, slot = operation(jobs)
    print(slot)
    print(total)


if __name__ == '__main__':
    main()


class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[[0 for col in range(v)] for row in range(v)]
    def mindist(self,dist,truth):
        min=float('inf')
        index=-1
        for i in range(self.v):
            if min>dist[i] and not truth[i]:
                min=dist[i]
                index=i
        return index
    def printsol(self,dist):
        print('distance of respective vertices from source ar:')
        for i in range(len(dist)):
            print(f'{i+1}:{dist[i]}')
    def dijkstra(self,start):
        dist=[float('inf')]*self.v
        dist[start]=0
        truth=[False]*self.v

        for i in range(self.v):
            u=self.mindist(dist,truth)
            truth[u]=True
            for j in range(self.v):
                if self.graph[u][j]>0 and not truth[j] and dist[j]> dist[u] + self.graph[u][j]:
                    dist[j]=dist[u] + self.graph[u][j]

        self.printsol(dist)

def adjecency(V):
    mat=[]
    for i in range(V):
        row=list(map(int,input(f'enter {i+1} row elements:').split()))
        if len(row)!=V:
            print('enter correct number of elements for the given row.')
            return
        mat.append(row)
    return mat
def main():
    V=int(input('Enter the number of vertices:'))
    g=Graph(V)
    g.graph=adjecency(V)
    src=int(input('enter the source index:'))
    g.dijkstra(src)

if __name__=='__main__':
    main()

def solve(graph):
    v=len(graph)
    dist=[row[:] for row in graph]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def main():
    v=int(input('enter the number of vertices:'))
    print('enter the graph details in form Starting vertex-ending vertex and weight. press done when done entering')
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
            print("Invalid inpute please enter the edge in the correct format.")
    result=solve(graph)
    print(result)

if __name__ == '__main__':
    main()
def isvalid(x,y,n,board):
    return 0<=x<n and 0<=y<n and board[x][y]==-1

def knight(x,y,board,cnt,moves,n):

    if cnt==n*n:
        return True
    for move in moves:
        nx,ny=x+move[0],y+move[1]
        if isvalid(nx,ny,n,board):
            board[nx][ny]=cnt
            if knight(nx,ny,board,cnt+1,moves,n):
                return True
            board[nx][ny]=-1
    return False
def main():
    N=int(input('Enter size of board:'))
    x=int(input('Enter starting row:'))
    y=int(input('enter starting column:'))
    board=[[-1 for _ in range(N)] for _ in range(N)]
    moves=[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    board[x][y]=0
    cnt=1
    if knight(x,y,board,cnt,moves,N):
        print(board)
    else:
        print('no solution exist.')

if __name__=='__main__':
    main()

class Assignment:
    def __init__(self,mat):
        self.matrix=mat
        self.n=len(mat)
        self.mincost=float('inf')
        self.best=None
    def b_b(self,dist,assignment):
        if dist==self.n:
            cost=sum(self.matrix[i][assignment[i]] for i in range(dist))
            if self.mincost>cost:
                self.mincost=cost
                self.best=assignment[:]
            return
        for i in range(self.n):
            if i not in assignment:
                assignment.append(i)
                self.b_b(dist+1,assignment)
                assignment.pop()

    def solve(self):
        self.b_b(0,[])
        return self.best,self.mincost
def main():
    n=int(input('Enter he no of stduents(and clubs):'))
    print('enter the cost matrix:')
    mat=[]
    for i in range(n):
        row=list(map(int,input(f'row {i+1}').split()))
        mat.append(row)
    a=Assignment(mat)
    best_assignment,cost=a.solve()
    print('Minimum cost is:',cost)
    print('Best assignment is:',best_assignment)

if __name__=='__main__':
    main()