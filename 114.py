class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        if root == None:
            return None
        self.dfs(root)
        
    def dfs(self, root):
        if root.left == None and root.right == None:
            return root, root
        
        head, tail = root, root
        left_head, left_tail = None, None
        right_head, right_tail = None, None
        
        if root.left:
            left_head, left_tail = self.dfs(root.left)
        if root.right:
            right_head, right_tail = self.dfs(root.right)
        
        if left_head:
            root.right = left_head
            left_tail.right = right_head
        
        tail = right_tail if right_tail else left_tail
        head.left = None
        return head, tail
        
root = TreeNode(0)
solution = Solution()
solution.flatten(root)
