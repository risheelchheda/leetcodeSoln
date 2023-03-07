res = [0]

        def dfs(node):
            if node is None:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

            
        dfs(root)
        return res[0]
