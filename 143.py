length=0
        arr=[]
        current=head
        while current:
            arr.append(current)
            length+=1
            current=current.next
        left=0
        right=length-1
        last=head
        while right>left:
            arr[left].next=arr[right]
            arr[right].next=arr[left+1]
            right-=1
            left+=1
            if arr[right]==arr[left]:
                arr[right].next=arr[left]
            last=arr[left]
        if last:
            last.next=None
        
        return head
