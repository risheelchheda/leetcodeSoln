if head==None:
            return head
        l1Head=ListNode(0)
        l2Head=ListNode(x)
        currentNode=head
        l1=l1Head
        l2=l2Head
        while currentNode:
            if currentNode.val>=x:
                l2.next=currentNode
                l2=l2.next
            else:
                l1.next=currentNode
                l1=l1.next
            currentNode=currentNode.next
        l2.next=None
        l1.next=l2Head.next
        return l1Head.next
