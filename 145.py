class TreeNode(object):
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        if root != None:
            if root.left != None:
                temp = self.postorderTraversal(root.left)
                for v in temp:
                    result.append(v)
            if root.right != None:
                temp = self.postorderTraversal(root.right)
                for v in temp:
                    result.append(v)
            result.append(root.val)
        return result