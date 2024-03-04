# https://leetcode.com/problems/binary-tree-right-side-view/


# For left view
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue=[]
        queue.append(root)
        result=[]
        while(queue):
            curr_result=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node:
                    curr_result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curr_result:
                result.append(curr_result[-1])
                print(result)
        return result

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

 



#FOr right node
    
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,2,5]
    
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue=[]
        queue.append(root)
        result=[]
        while(queue):
            curr_result=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                if node:
                    curr_result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curr_result:
                result.append(curr_result[0])
                print(result)
        return result