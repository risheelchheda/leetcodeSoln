stack=[]
        curr=root
        while True:
            while curr:
                stack.append(curr)
                curr=curr.left
            if stack==[]:
                break
            node=stack.pop()
            k-=1
            if k==0:
                return node.val
            curr=node.right
