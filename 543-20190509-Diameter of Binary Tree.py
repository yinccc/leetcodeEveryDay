# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = 0
        self.diameter(root)
        return self.d

    def diameter(self, root):
        if root == None:
            return 0
        l, r = self.diameter(root.left), self.diameter(root.right)
        self.d = max(self.d, l + r)
        return max(l, r) + 1