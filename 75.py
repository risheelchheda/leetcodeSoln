left=0
        current=0
        right=len(nums)-1
        while current<=right:
            if nums[current]==0:
                nums[current],nums[left]=nums[left],nums[current]
                left+=1
                current+=1
            elif nums[current]==2:
                nums[right],nums[current]=nums[current],nums[right]
                right-=1
            else:
                current+=1
