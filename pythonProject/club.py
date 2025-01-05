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