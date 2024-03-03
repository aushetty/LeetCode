#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/


#103. Binary Tree Zigzag Level Order Traversal



# Given the root of a binary tree, return the zigzag level order traversal
# of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

                # queue=([root] if root else return)
        queue = [root]

        result = []
        flag = True

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


                result.append(curr_result[::-1] if flag == False else curr_result)
                flag = not flag
                print(result)
        return result           

        
        