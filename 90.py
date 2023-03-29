def solve(start,subset):
            if subset not in res:
                res.append(subset[:])
            for i in range(start,len(nums)):
                subset.append(nums[i])
                solve(i+1,subset)
                subset.pop()
        nums.sort()
        res=[]
        solve(0,[])
        return res
