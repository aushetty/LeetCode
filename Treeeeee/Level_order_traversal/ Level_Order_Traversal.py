# https://leetcode.com/problems/binary-tree-level-order-traversal/


#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


#Input: root = [3,9,20,null,null,15,7]





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def levelOrder(self, root):

        queue = [root]

        result = []
        if not root:
            return []



        while queue:

            curr_result = []

            for i in range(len(queue)):
                node = queue.pop(0)

                curr_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_result)

        return result 








#Better solution
    

        # queue=[]
        # queue.append(root)
        # result=[]
        # while(queue):
        #     curr_result=[]
        #     for i in range(len(queue)):
        #         node=queue.pop(0)
        #         if node:
        #             curr_result.append(node.val)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if curr_result:
        #         result.append(curr_result)
        # return result
