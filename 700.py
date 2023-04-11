curr=root
        while curr:
            if curr.val==val:
                return curr
            if val>curr.val:
                curr=curr.right
            else:
                curr=curr.left
        return curr
