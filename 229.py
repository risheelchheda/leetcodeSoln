count1=0
        count2=0
        num1=None
        num2=None
        for i in nums:
            if i==num1:
                count1+=1
            elif i==num2:
                count2+=1
            elif count1==0:
                num1=i
                count1=1
            elif count2==0:
                num2=i
                count2=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in nums:
            if i==num1:
                count1+=1
            if i==num2:
                count2+=1
        l=len(nums)
        res=[]
        if count1>l//3:
            res.append(num1)
        if count2>l//3 and num2!=num1:
            res.append(num2)
        return res
