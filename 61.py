if head==None:
            return head
        if head.next==None or k==0 :
            return head
        currentNode=head
        length=0
        while currentNode:
            currentNode=currentNode.next
            length+=1
        if k%length==0:
            return head
        for i in range(k%length):
            dummyHead=ListNode(0)
            currentNode=head
            while currentNode.next.next:
                currentNode=currentNode.next
            nextNode=currentNode.next
            dummyHead.next=nextNode
            nextNode.next=head
            currentNode.next=None
            head=dummyHead.next
        return dummyHead.next
