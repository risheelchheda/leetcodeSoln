#TOP DOWN APPROACH
def solve(values,i,j,dp):
      if i+1==j:
          return 0
      if dp[i][j]!=-1:
          return dp[i][j]
      ans=1e9
      for k in range(i+1,j):
          ans=min(ans,values[i]*values[j]*values[k]+solve(values,i,k,dp)+solve(values,k,j,dp))
          dp[i][j]=ans
      return ans

  n=len(values)
  dp=[[-1 for i in range(n)] for i in range(n)]
  return solve(values,0,len(values)-1,dp)

#BOTTOM UP APPROACH
n=len(values)
dp=[[0 for i in range(n)] for i in range(n)]
for i in range(n-1,-1,-1):
    for j in range(i+2,n):
        ans=1e9
        for k in range(i+1,j):
            ans=min(ans,values[i]*values[j]*values[k]+dp[i][k]+dp[k][j])
            dp[i][j]=ans
return dp[0][n-1]
      
