if head.next==None and n==1:
            head=None
            return head
        length=0
        currentNode=head
        while currentNode:
            currentNode=currentNode.next
            length+=1
        loc=length-n+1

        if length==n:
            return head.next
        
        length=0
        currentNode=head
        while currentNode:
            length+=1
            if length==loc-1:
                currentNode.next=currentNode.next.next
            currentNode=currentNode.next
        return head
