in_map={val:i for i,val in enumerate(inorder)}
        def build_tree(pre_start,pre_end,in_start,in_end):
            if pre_start>pre_end:
                return None
            val=preorder[pre_start]
            root=TreeNode(val)
            ind=in_map[val]
            left_size=ind-in_start
            root.left=build_tree(pre_start+1,pre_start+left_size,in_start,ind-1)
            root.right=build_tree(pre_start+left_size+1,pre_end,ind+1,in_end)
            return root
        
        return build_tree(0,len(preorder)-1,0,len(inorder)-1)
