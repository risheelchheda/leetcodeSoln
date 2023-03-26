nums.sort()
        if len(nums)<=1:
            return False
        if nums[0]==nums[1]:
            return True
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
