#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

        return root

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)

a.left=b
a.right=e
b.left=c
b.right=d
e.right=f

S=Solution()
print(S.flatten(a).right.right.right.val)

