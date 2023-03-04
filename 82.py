if head==None:
            return head
        dummyHead=ListNode(-100)
        dummyHead.next=head
        prev=dummyHead
        current=head
        dup=dummyHead.val
        while current.next:
            if current.val==current.next.val or current.val==dup:
                dup=current.val
                prev.next=current.next
                current=current.next
            else:
                dup=current.val
                prev=current
                current=current.next
        if current.val==dup:
            prev.next=None
        return dummyHead.next
