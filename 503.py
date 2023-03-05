res=[-1 for i in range(len(nums))]
        stack=[]
        for i in range(2*len(nums)):
            curr=nums[i%len(nums)]
            while stack and curr>nums[stack[-1]]:
                ind=stack.pop()
                res[ind]=curr
            stack.append(i%len(nums))
        return res
