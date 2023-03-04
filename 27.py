if val in nums:
            c=nums.count(val)
            for i in range(c):
                nums.remove(val)
            return len(nums)
