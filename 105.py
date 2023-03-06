in_map={val:i for i,val in enumerate(inorder)}
        def build(start,end):
            if start>end:
                return None
            
            val=preorder.pop(0)
            root=TreeNode(val)
            ind=in_map[val]

            root.left=build(start,ind-1)
            root.right=build(ind+1,end)
            return root
        
        return build(0,len(inorder)-1)
