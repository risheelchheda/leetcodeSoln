if root==None:
            return 0
        count=0
        stack=[root]
        while stack:
            node=stack.pop()
            count+=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count
