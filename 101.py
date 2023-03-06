def isSame(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val!=q.val:
                return False
            else:
                return isSame(p.right,q.left) and isSame(p.left,q.right)
        
        ans=isSame(root.left,root.right)
        return ans
