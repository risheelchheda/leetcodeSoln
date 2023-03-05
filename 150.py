if len(tokens)==1:
            return int(tokens[0])
        stack=[]
        for i in tokens:
            if i =="+":
                ans=stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif i =="-":
                ans=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif i =="*":
                ans=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(ans)
            elif i =="/":
                ans=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ans)
            else:
                stack.append(int(i))
            
        return ans
