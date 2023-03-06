if root==None:
            return root
        res=[]
        curr=root
        stack=[]
        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                curr=curr.right
        return res
