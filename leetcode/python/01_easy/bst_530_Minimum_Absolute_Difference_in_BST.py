# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ordered = []
        minVal = float('inf')

        def inorder(root):
            if root:
                inorder(root.left)
                ordered.append(root.val)
                inorder(root.right)

        inorder(root)

        for i in range(1, len(ordered)):
            minVal = min(minVal, ordered[i]-ordered[i-1])

        return minVal