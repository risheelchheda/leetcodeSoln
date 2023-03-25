if nums==[]:
            return 0
        nums.sort()
        res=[]
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                if count>1:
                    res.append(count)
                count=1
        res.append(count)
        res.sort()
        return res[-1]
