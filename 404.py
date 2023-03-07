if root==None:
            return 0
        sum=0
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left and node.left.left==None and node.left.right==None:
                sum+=node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sum
