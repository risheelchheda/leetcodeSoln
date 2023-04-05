res=[]
        n=len(s)
        tmp=''
        for i in range(n,0,-1):
            if s[i-1]==' ':
                if tmp!='':
                    res.append(tmp)
                    tmp=''
            else:
                tmp=s[i-1]+tmp
        if tmp!='':
            res.append(tmp)
        return " ".join(res)
