#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/1192644114/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue= [root]

        result = []

        if not root:
            return

        while queue:

            curr_result = []
            for i in range(len(queue)):
                node = queue.pop(0)

                if node:
                    curr_result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if curr_result:
                result.append(curr_result)
        return result[::-1]             
    


#     Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]