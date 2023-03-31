l=0
        r=x
        while r>=l:
            mid=(l+r)//2
            square=mid*mid
            if square==x:
                return mid
            elif square>x:
                r=mid-1
            else:
                l=mid+1
        return r
