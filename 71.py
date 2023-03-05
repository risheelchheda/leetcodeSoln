arr=path.split("/")
        stack=[]
        for i in arr:
            if len(i)>0 and i!=".":
                if i==".." and stack:
                    stack.pop()
                elif i!="..":
                    stack.append(i)
        return "/"+"/".join(stack)
