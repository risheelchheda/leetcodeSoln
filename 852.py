l=0
        r=len(arr)
        while l>=0:
            if arr[l]<arr[l+1]:
                l+=1
            else:
                return l
