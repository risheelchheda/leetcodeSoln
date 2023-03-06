if root==None:
            return root
        res=[]
        qu=[root]
        while qu:
            level=[]
            for i in range(len(qu)):
                node = qu.pop(0)
                level.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(level)
        return res
