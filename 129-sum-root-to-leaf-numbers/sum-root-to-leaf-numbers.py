# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, num):
            if cur == None:
                return 0

            num = num * 10 + cur.val
            if cur.left == None and cur.right == None:
                return num

            return dfs(cur.left, num) + dfs(cur.right, num)


        return dfs(root, 0)