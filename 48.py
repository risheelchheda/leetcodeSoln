from copy import deepcopy
        a=deepcopy(matrix)
        for i in range(len(a)):
            for j in range(len(a[0])):
                matrix[i][j]=a[-j-1][i]
