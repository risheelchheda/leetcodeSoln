if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
