#TOP BOTTOM APPROACH
from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        def solve(arr,n,time,dp):
            if n>=len(arr):
                return 0
            if dp[n][time]!=-1:
                return dp[n][time]
            incl=(arr[n]*(time+1))+solve(arr,n+1,time+1,dp)
            excl=solve(arr,n+1,time,dp)
            dp[n][time]=max(incl,excl)
            return dp[n][time]


        satisfaction=sorted(satisfaction)
        n=len(satisfaction)
        dp=[[-1 for i in range(n)] for i in range(n)]
        return solve(satisfaction,0,0,dp)
      
 #BOTTOM UP APPROACH
n = len(satisfaction)
        satisfaction.sort()
        
        dp = [0] * (n + 1)
        
        for dish in range(n - 1, -1, -1):
            nxt_dp = [0] * (dish + 1)
            for time in range(dish, -1, -1):
                cook = satisfaction[dish] * (time + 1) + dp[time + 1]
                skip = dp[time]
                nxt_dp[time] = max(cook, skip)
            dp = nxt_dp
        
        return dp[0]
