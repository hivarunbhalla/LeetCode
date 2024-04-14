# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def ans(node):
        if node== None:
            return 0
        sum = 0
        if node.left and (node.left.left == node.left.right  == None):
            sum += node.left.val

        return sum + ans(node.left) + ans(node.right)

class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            return ans(root)

        