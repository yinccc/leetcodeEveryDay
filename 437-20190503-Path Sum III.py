class Solution(object):
    cnt = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.find(root, sum)
        return self.cnt

    def find(self, root, sum):
        if root == None:
            return
        self.path(root, sum)
        self.find(root.left, sum)
        self.find(root.right, sum)

    def path(self, root, sum):
        if root == None:
            return
        if (sum - root.val == 0):
            self.cnt += 1
        self.path(root.left, sum - root.val)
        self.path(root.right, sum - root.val)
