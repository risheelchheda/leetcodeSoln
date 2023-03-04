if head==None:
            return head
        elif head.next==None:
            return head
        dummyHead=ListNode(0)
        dummyHead.next=head
        current=head.next
        head.next=None
        while current:
            nextNode=current.next
            current.next=dummyHead.next
            dummyHead.next=current
            current=nextNode
        return dummyHead.next
