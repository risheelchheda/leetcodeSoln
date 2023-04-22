#TOP DOWN APROACH
def solve(index,end,slices,n,dp):
    if n==0 or index>end:
        return 0
    if dp[index][n]!=-1:
        return dp[index][n]
    incl=slices[index]+solve(index+2,end,slices,n-1,dp)
    excl=solve(index+1,end,slices,n,dp)
    dp[index][n]=max(incl,excl)
    return dp[index][n]

k=len(slices)
dp=[[-1 for i in range(k+1)] for i in range(k)]
case1=solve(0,k-2,slices,int(k/3),dp)
dp=[[-1 for i in range(k+1)] for i in range(k)]
case2=solve(1,k-1,slices,int(k/3),dp)
return max(case1,case2)

#BOTTOM UP APPROACH
k=len(slices)
        dp=[[0 for i in range(k+1)] for i in range(k+1)]
        for index in range(k-2,-1,-1):
            for n in range(1,k//3+1):
                incl=slices[index]+dp[index+2][n-1]
                excl=dp[index+1][n]
                dp[index][n]=max(incl,excl)
        case1=dp[0][k//3]
        dp=[[0 for i in range(k+2)]for i in range(k+2)]
        for index in range(k-1,0,-1):
            for n in range(1,k//3+1):
                incl=slices[index]+dp[index+2][n-1]
                excl=dp[index+1][n]
                dp[index][n]=max(incl,excl)
        case2=dp[1][k//3]
        return max(case1,case2)
      
 #OPTIMISED SOLUTION
k=len(slices)
        prev1=[0 for i in range(k+1)]
        curr1=[0 for i in range(k+1)]
        next1=[0 for i in range(k+1)]
        for index in range(k-2,-1,-1):
            for n in range(1,k//3+1):
                incl=slices[index]+next1[n-1]
                excl=curr1[n]
                prev1[n]=max(incl,excl)
            next1=curr1
            curr1=prev1
        case1=curr1[k//3]
        prev2=[0 for i in range(k+2)]
        curr2=[0 for i in range(k+2)]
        next2=[0 for i in range(k+2)]
        for index in range(k-1,0,-1):
            for n in range(1,k//3+1):
                incl=slices[index]+next2[n-1]
                excl=curr2[n]
                prev2[n]=max(incl,excl)
            next2=curr2
            curr2=prev2
        case2=curr2[k//3]
        return max(case1,case2)
