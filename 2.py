dummyhead=ListNode(0)
        currentNode=dummyhead
        carry=0
        while l1!=None  or l2!=None or carry!=0:
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            s=(l1val+l2val+carry)%10
            carry=(l1val+l2val+carry)//10
            nextNode=ListNode(s)
            currentNode.next=nextNode
            currentNode=nextNode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummyhead.next
