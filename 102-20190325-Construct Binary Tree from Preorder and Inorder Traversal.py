#这个类有毒？？？？？
class BinaryTree:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class TreeNode2:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = BinaryTree(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


class Solution:
    def PreorderInorder(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = BinaryTree(inorder[ind])
            root.left = self.PreorderInorder(preorder, inorder[0:ind])
            root.right = self.PreorderInorder(preorder, inorder[ind + 1:])
            return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
S = Solution()
S2 = Solution2()
# print(S.PreorderInorder(preorder,inorder))
print(S2.buildTree(preorder, inorder).val)
