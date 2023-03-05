numbers=[str(i) for i in range(10)]
        string=""
        curr_num=0
        stack=[]
        for i in s:
            if i in numbers:
                curr_num=curr_num*10+int(i)
            elif i=="[":
                stack.append(curr_num)
                stack.append(string)
                curr_num=0
                string=""
            elif i=="]":
                prev_str=stack.pop()
                num=stack.pop()
                string=prev_str+string*num
            else:
                string+=i
        while stack:
            string=stack.pop()+string
        return string
