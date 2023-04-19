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
