isDummy=False
        if head==None:
            return head
        elif head.next==None:
            return head
        if left==1:
            dummyHead=ListNode(0)
            dummyHead.next=head
            head=dummyHead
            right=right+1
            left=left+1
            isDummy=True
        rightNode=leftNode=prev=head
        for i in range(right-1):
            rightNode=rightNode.next
        for i in range(left-1):
            leftNode=leftNode.next
            if i!=left-2:
                prev=prev.next
        nextNode=leftNode
        currentNode=leftNode.next
        for i in range(right-left):
            nextNode.next=currentNode.next
            currentNode.next = prev.next
            prev.next=currentNode
            currentNode=nextNode.next
        if isDummy:
            return head.next
        return head
            
