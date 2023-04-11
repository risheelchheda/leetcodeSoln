if not root:
            return root
        res=[]
        height=1
        qu=[root]
        while qu:
            for i in range(height-1):
                node=qu.pop(0)
                nextNode=qu[0]
                node.next=nextNode
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            node=qu.pop(0)
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
            height*=2
        return root
