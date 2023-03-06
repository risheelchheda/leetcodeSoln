length=arr[-1]+k
        missing=[]
        for i in range(1,length+1):
            if i not in arr:
                missing.append(i)
        return missing[k-1]
