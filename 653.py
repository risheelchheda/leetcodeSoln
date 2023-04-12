stack_left, stack_right = [], []
        curr_left, curr_right = root, root
        while True:
            # Inorder traversal from the left subtree
            while curr_left:
                stack_left.append(curr_left)
                curr_left = curr_left.left

            # Inorder traversal from the right subtree
            while curr_right:
                stack_right.append(curr_right)
                curr_right = curr_right.right

            # If we have exhausted both the stacks or found a pair of elements
            if not stack_left or not stack_right or stack_left[-1] == stack_right[-1]:
                return False
            left_val, right_val = stack_left[-1].val, stack_right[-1].val
            if left_val + right_val == k:
                return True
            elif left_val + right_val < k:
                curr_left = stack_left.pop().right
            else:
                curr_right = stack_right.pop().left
