def check(row,col,n,board):
            for i in range(n):
                if board[i][col]=="Q":
                    return False
            i,j=row,col
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i,j=row,col
            while i>=0 and j<n:
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
        
        def solve(row,n,board,res):
            if row==n:
                res.append(["".join(i) for i in board])
                return
            for col in range(n):
                if check(row,col,n,board):
                    board[row][col]='Q'
                    solve(row+1,n,board,res)
                    board[row][col]="."
            return
    
        res=[]
        board=[["." for i in range(n)] for j in range(n)]
        solve(0,n,board,res)
        return len(res)
