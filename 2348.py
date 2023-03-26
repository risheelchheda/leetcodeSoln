if 0 not in nums:
            return 0
        res=[]
        i=0
        n=len(nums)
        while n>i:
            if nums[i]==0:
                j=i+1
                while n>j and nums[j]==0:
                    j+=1
                res.append(j-i)
                i=j
            else:
                i+=1
        count=0
        for i in res:
            while i>0:
                count+=i
                i-=1
        return count
