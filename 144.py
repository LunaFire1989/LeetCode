class TreeNode(object):
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        result = []
        if root != None:
            result.append(root.val)
            if root.left != None:
                temp = self.preorderTraversal(root.left)
                for v in temp:
                    result.append(v)
            if root.right != None:
                temp = self.preorderTraversal(root.right)
                for v in temp:
                    result.append(v)
        return result