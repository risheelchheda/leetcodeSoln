#Top bottom approach
def solve(n,dp,cost):
            if n<=1:
                return cost[n]
            if dp[n]!=-1:
                return dp[n]
            dp[n]=min(solve(n-1,dp,cost),solve(n-2,dp,cost))+cost[n]
            return dp[n]

        n=len(cost)
        cost.append(0)
        dp=[-1 for i in range(n+1)]
        return solve(n,dp,cost)

#Bottom up approach
n=len(cost)
        cost.append(0)
        dp=[-1 for i in range(n+1)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n+1):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return dp[n]

#Optimised Solution
n=len(cost)
        cost.append(0)
        a=cost[0]
        b=cost[1]
        if n==0:
            return a
        for i in range(2,n+1):
            curr=min(a,b)+cost[i]
            a=b
            b=curr
        return b
