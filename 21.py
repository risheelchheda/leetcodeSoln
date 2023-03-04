head=ListNode(val=0)
        currentNode=head
        while list1 and list2:
            if list1.val>=list2.val :
                currentNode.next=ListNode(list2.val)
                list2=list2.next
            else:
                currentNode.next=ListNode(list1.val)
                list1=list1.next
            currentNode=currentNode.next
        while list1 or list2:
            if list2==None and list1:
                currentNode.next=ListNode(list1.val)
                list1=list1.next
            elif list1==None and list2:
                currentNode.next=ListNode(list2.val)
                list2=list2.next
            currentNode=currentNode.next
        return head.next
