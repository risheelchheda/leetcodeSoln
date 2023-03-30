def solve(start):
            if start==len(nums):
                res.append(nums[:])
                return
                
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                solve(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        res=[]
        solve(0)
        return res
