if head==None or head.next==None:
            return head
        dummyHead=ListNode(0)
        dummyHead.next=head
        prev=dummyHead
        p=head
        while p!=None and p.next!=None:
            q=p.next
            r=p.next.next
            prev.next=q
            q.next=p
            p.next=r
            prev=p
            p=r
        return dummyHead.next
