row=0
        for i in range(len(matrix)):
            if target>=matrix[i][0]:
                row=i
        l=0
        r=len(matrix[row])-1
        while r>=l:
            mid=(l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
