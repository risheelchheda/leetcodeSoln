if root==None:
            return root
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        root=res.pop(0)
        while res:
            root.right=res.pop(0)
            root.left=None
            root=root.right
        return root
