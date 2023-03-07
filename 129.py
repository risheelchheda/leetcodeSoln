res=[]
        stack=[(root,root.val)]
        while stack:
            node,val=stack.pop()
            if node.left==None and node.right==None:
                res.append(val)
            if node.left:
                stack.append((node.left,val*10+node.left.val))
            if node.right:
                stack.append((node.right,val*10+node.right.val))
        return sum(res)
