if root==None:
            return 0
        res=[]
        height=1
        stack=[(root,height)]
        while stack:
            node,height=stack.pop()
            if node.left==None and node.right==None:
                res.append(height)
            if node.left:
                stack.append((node.left,height+1))
            if node.right:
                stack.append((node.right,height+1))
        return min(res)
