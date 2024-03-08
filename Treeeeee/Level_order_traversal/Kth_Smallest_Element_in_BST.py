# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Input: root = [3,1,4,null,2], k = 1
# Output: 1





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        result = []


        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result[k-1]
    




    # Use iterative approach for DFS stack and then when you get the array in sorted manner return the k-1 indexed value from the array


