res=[]
        a=''
        stack=[]
        for i in s:
            if i not in a:
                a+=i
            else:
                ind=a.index(i)
                a=a[ind+1:]
                a+=i
            res.append(a)
        m=0
        for i in res:
            if len(i)>m:
                m=len(i)
        print(res)
        return m
