def solveNQueens(self, n: int) -> List[List[str]]:
        def safe(row,col,n,matrix):
            for i in range(n):
                if matrix[i][col]=="Q":
                    return False
            i,j=row,col
            while(i>=0 and j>=0):
                if(matrix[i][j] == "Q"):
                    return False
                i -= 1
                j -= 1
            i,j = row,col
            while(i>=0 and j<n):
                if(matrix[i][j] == "Q"):
                    return False
                i -= 1
                j += 1
            return True
            



        def solve(row,n,matrix,res):
            if row==n:
                res.append(["".join(i) for i in matrix])
                return
            for col in range(n):
                if safe(row,col,n,matrix):
                    matrix[row][col]='Q'
                    solve(row+1,n,matrix,res)
                    matrix[row][col]="."
            return
                
        
        res=[]
        matrix=[["." for i in range(n)] for j in range(n)]
        solve(0,n,matrix,res)           
        return res 
