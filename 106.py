in_map={val:i for i,val in enumerate(inorder)}
        def build(start, end):
            if start > end:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            
            index = in_map[val]
            
           
            node.right = build(index + 1, end)
            node.left = build(start, index - 1)
            
            return node
        
        return build(0, len(inorder) - 1)
