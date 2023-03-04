 arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
        dummy=ListNode(0)
        dummy.next=head
        current=head.next
        head.next=None
        while current:
            nextNode=current.next
            current.next=dummy.next
            dummy.next=current
            current=nextNode
        rev=[]
        current=dummy.next
        while current:
            rev.append(current.val)
            current=current.next
        for i in range(len(arr)):
            if arr[i]!=rev[i]:
                return False
        return True
