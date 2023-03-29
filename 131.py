res=[]
        tmp=[]
        def is_palindrome(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def solve(start):
            if start>=len(s):
                res.append(tmp[:])
                return
        
            for i in range(start,len(s)):

                if is_palindrome(s,start,i):
                    tmp.append(s[start:i+1])
                    solve(i+1)
                    tmp.pop()
        solve(0)
        return res
