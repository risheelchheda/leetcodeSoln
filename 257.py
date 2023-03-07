stack=[(root,str(root.val))]
        res=[]
        while stack:
            node,s=stack.pop()
            if node.right==None and node.left==None:
                res.append(s)
            if node.right:
                stack.append((node.right,s+"->"+str(node.right.val)))
            if node.left:
                stack.append((node.left,s+"->"+str(node.left.val)))
        return res
