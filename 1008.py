root=TreeNode(preorder[0])
        parent=root
        stack=[root]
        for i in preorder[1:]:
            newNode=TreeNode(i)
            if stack and newNode.val<parent.val:
                parent.left=newNode
                stack.append(newNode)
                parent=newNode
            else:
                while stack and stack[-1].val<newNode.val:
                    parent=stack.pop()
                parent.right=newNode
                stack.append(newNode)
                parent=newNode
        return root
