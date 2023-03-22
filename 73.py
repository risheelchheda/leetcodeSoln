m=len(matrix)
        n=len(matrix[0])
        col=[]
        row=[]
        for i in range(m):
            if 0 in matrix[i]:
                row.append(i)
                for j in range(n):
                    if matrix[i][j]==0:
                        if j not in col:
                            col.append(j)
        for i in matrix:
            for j in col:
                i[j]=0
        for i in row:
            matrix[i]=[0]*n
        
