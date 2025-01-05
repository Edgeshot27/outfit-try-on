def isvalid(x,y,board):
    return 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]==-1
def knight(x,y,board,cnt,moves,n):
    if cnt==n*n:
        return True
    for move in moves:
        nx,ny=x+move[0],y+move[1]
        if isvalid(nx,ny,board):
            board[nx][ny]=cnt
            if knight(nx,ny,board,cnt+1,moves,n):
                return True
            board[nx][ny]=-1
    return False
def main():
    n=int(input('enter size of board:'))
    board=[[-1 for col in range(n)] for row in range(n)]
    x=int(input('enter starting row:'))
    y=int(input('enter starting column:'))
    board[x][y]=0
    cnt=1
    moves=[(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
    if knight(x,y,board,cnt,moves,n):
        print(board)

if __name__=='__main__':
    main()