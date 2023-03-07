if root==None or root==p or root==q:
            return root
        
        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)
        
        if l and r:
            return root
        return l or r
