if root==None:
            return 0
        res=[]
        qu=[root]
        while qu:
            nodelink=[]
            for i in range(len(qu)):
                node=qu.pop(0)
                nodelink.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            res.append(nodelink)
        return len(res)
