maxsum=nums[0]
        currsum=nums[0]
        for i in nums[1:]:
            currsum+=i
            if i>currsum:
                currsum=i
            maxsum=max(maxsum,currsum)
        return maxsum
