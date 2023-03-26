if digits=="":
            return []
        res=['']
        mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for i in digits:
            tmp=[]
            for j in mapping[i]:
                for k in res:
                    tmp.append(k+j)
            res=tmp
        return res
