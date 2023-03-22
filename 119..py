Pascal=[[0 for j in range(i)]for i in range(1,rowIndex+2)]
        row=[]
        for i in range(rowIndex+1):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]= Pascal[i-1][j-1] + Pascal[i-1][j]
            Pascal[i]=row
        return row
