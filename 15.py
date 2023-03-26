res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l,r=i+1,n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    arr=[nums[i],nums[l],nums[r]]
                    if arr not in res:
                        res.append(arr)
                    if l<r and nums[l]==nums[l+1]:
                        l+=1
                    if l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return res
