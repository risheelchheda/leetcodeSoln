if not root:
      return None

    left = root.left
    right = root.right
    root.left = self.invertTree(right)
    root.right = self.invertTree(left)
    return root
