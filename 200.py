def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0' or visited[i][j]:
                return 
            visited[i][j]=True
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        m=len(grid)
        n=len(grid[0])
        visited=[[False for i in range(n)]for j in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    dfs(i,j)
        return coun
