 dict={val:i for i,val in enumerate(nums1)}
        res=[-1 for i in range(len(nums1))]
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                ind=dict[val]
                res[ind]=curr
            if curr in nums1:
                stack.append(curr)
        return res
