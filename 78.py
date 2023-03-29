def solve(start,subset):
            res.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                solve(i+1,subset)
                subset.pop()
        res=[]
        solve(0,[])
        return res
