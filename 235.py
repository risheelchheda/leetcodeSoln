curr=root
        while curr:
            if (p.val>curr.val and q.val<curr.val) or (q.val>curr.val and p.val<curr.val):
                return curr
            elif p.val<curr.val and q.val<curr.val:
                curr=curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr=curr.right
            elif p.val==curr.val or q.val==curr.val:
                return curr
