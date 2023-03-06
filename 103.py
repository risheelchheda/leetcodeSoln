if root==None:
            return root
        res=[]
        qu=[root]
        right=True
        while qu:
            nodelink=[]
            for i in range(len(qu)):
                node=qu.pop(0)
                nodelink.append(node.val)
                if node.left:
                        qu.append(node.left)
                if node.right:
                        qu.append(node.right)
            if right:
                right=False
            else:
                right=True
                nodelink=nodelink[::-1]
            res.append(nodelink)
        return res
