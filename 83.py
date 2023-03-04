if head==None:
            return head
        if head.next==None:
            return head
        prev=head
        current=head.next
        while current.next:
            if prev.val==current.val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        if current.val==prev.val:
            prev.next=None
        return head
