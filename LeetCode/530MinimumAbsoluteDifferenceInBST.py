def getMinimumDifference(root):
    def dfs(node, l=[]):
        if node.left is not None:
            dfs(node.left, l)
        l.append(node.val)
        if node.right is not None:
            dfs(node.right, l)
        return l

    l = dfs(root)
    return min(abs(a - b) for a, b in zip(l, l[1:]))

