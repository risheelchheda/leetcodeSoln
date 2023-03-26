nums.sort()
        res={}
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while r>l:
                sum=nums[i]+nums[r]+nums[l]
                res[abs(sum-target)]=sum
                if sum>target:
                    r-=1
                else:
                    l+=1
        closest=min(res)
        return res[closest]
