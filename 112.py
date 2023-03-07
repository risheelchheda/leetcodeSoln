if root==None:
            return root
        stack=[(root,root.val)]
        while stack:
            node,val=stack.pop()
            if node.right==None and node.left==None and val==targetSum:
                return True
            if node.left:
                stack.append((node.left,val+node.left.val))
            if node.right:
                stack.append((node.right,val+node.right.val))
        return False
