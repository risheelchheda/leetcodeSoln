if root==None:
            return root
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
        ans=[]
        for i in res:
            ans.append(i[-1])
        return ans
