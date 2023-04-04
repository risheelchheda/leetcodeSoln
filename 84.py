n=len(heights)
        #Finding the right smallest element of each element in the array
        right_small=[]
        stack=[]
        for i in range(n,0,-1):
            while stack and heights[stack[-1]]>=heights[i-1]:
                stack.pop()
            if stack==[]:
                right_small.append(n)
            else:
                right_small.append(stack[-1])
            stack.append(i-1)
        right_small=right_small[::-1]
        #Finding the left smallest element of each element in the array
        stack=[]
        left_small=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack==[]:
                left_small.append(-1)
            else:
                left_small.append(stack[-1])
            stack.append(i)
        #Finding area for each block
        max_area=0
        for i in range(n):
            area=heights[i]*(right_small[i]-left_small[i]-1)
            max_area=max(max_area,area)
        return max_area
