#TOP DOWN APPROACH 
  def solve(prev1,prev2,index,swapped,dp):
    if index==len(nums1):
        return 0
    if dp[index][swapped]!=-1:
        return dp[index][swapped]
    ans=1e9
    if nums1[index]>prev1 and nums2[index]>prev2:
        ans= solve(nums1[index],nums2[index],index+1,0,dp)
    if nums1[index]>prev2 and nums2[index]>prev1:
        ans=min(ans,1+solve(nums2[index],nums1[index],index+1,1,dp))
    dp[index][swapped]=ans
    return dp[index][swapped]

dp=[[-1]*2 for i in range(len(nums1)+1)]
return int(solve(-1,-1,0,0,dp))

#BOTTTOM UP APPROACH
n=len(nums1)
        dp=[[0]*2 for i in range(n+1)]
        nums1.insert(0,-1)
        nums2.insert(0,-1)
        for index in range(n-1,0,-1):
            for swapped in range(1,-1,-1):
                ans=1e9
                prev1=nums1[index-1]
                prev2=nums2[index-1]
                if swapped==1:
                    prev1,prev2=prev2,prev1
                if nums1[index]>prev1 and nums2[index]>prev2:
                    ans= dp[index+1][0]
                if nums1[index]>prev2 and nums2[index]>prev1:
                    ans=min(ans,1+dp[index+1][1])
                dp[index][swapped]=ans
        return dp[1][0]
