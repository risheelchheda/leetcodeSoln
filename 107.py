if root==None:
            return root
        qu=[root]
        res=[]
        while qu:
            nodelist=[]
            for i in range(len(qu)):
                node=qu.pop(0)
                nodelist.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(nodelist)
        return res[::-1]
