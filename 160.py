if headA==None or headB==None:
            return None
        l1=headA
        l2=headB
        length1=0
        length2=0
        while l1:
            length1+=1
            l1=l1.next
        while l2:
            length2+=1
            l2=l2.next
        l1=headA
        l2=headB
        if length1>=length2:
            diff=length1-length2
            for i in range(diff):
                l1=l1.next
        else:
            diff=length2-length1
            for i in range(diff):
                l2=l2.next
        while l1 or l2:
            if l1==l2:
                return l1
            l1=l1.next
            l2=l2.next
        return None
