
#https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):


        def maxdepth(root):
            if not root:
                return 0

            left_depth = maxdepth(root.left)
            right_depth = maxdepth(root.right)

            # Add 1 for the current node
            return max(left_depth, right_depth) + 1

        return maxdepth(root)
    




# INput = root =
# [3,9,20,null,null,15,7]
    

#Output = 3
    
