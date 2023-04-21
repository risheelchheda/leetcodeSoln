#TOP BOTTOM APPROACH it is getting TLE
def solve(obstacle,lane,pos,dp):
            n=len(obstacle)-1
            if pos==n:
                return 0
            if dp[lane][pos]!=-1:
                return dp[lane][pos]
            if obstacle[pos+1]!=lane:
                return solve(obstacle,lane,pos+1,dp)
            else:
                ans=1e9
                for i in range(1,4):
                    if i!=lane and obstacle[pos]!=i:
                        ans=min(ans,1+solve(obstacle,i,pos,dp))
            dp[lane][pos]=ans
            return dp[lane][pos]


        
        dp=[[-1 for i in range(len(obstacles))]for i in range(4)]
        return solve(obstacles,2,0,dp)
      
#BOTTOM UP APPROACH
n=len(obstacles)-1
        dp=[[1e9 for i in range(len(obstacles))]for i in range(4)]
        dp[0][n]=0
        dp[1][n]=0
        dp[2][n]=0
        dp[3][n]=0

        for pos in range(n-1,-1,-1):
            for lane in range(1,4):
                if obstacles[pos+1]!=lane:
                    dp[lane][pos]=dp[lane][pos+1]
                else:
                    ans=float(inf)
                    for i in range(1,4):
                        if i!=lane and obstacles[pos]!=i:
                            ans=min(ans,1+dp[i][pos+1])
                    dp[lane][pos]=ans
        return min(dp[1][0]+1,dp[2][0],dp[3][0]+1)
