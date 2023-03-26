count=0
        res=[]
        for i in nums:
            if i==1:
                count+=1
            else:
                res.append(count)
                count=0
        res.append(count)
        return max(res)
