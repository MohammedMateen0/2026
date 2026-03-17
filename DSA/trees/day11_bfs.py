from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solutin:
    def level_order(self,root:TreeNode):
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level_legnth=len(queue)
            current_level=[]
            for _ in range(level_legnth):
                node=queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
if __name__=='__main__':
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.right.left=TreeNode(15)
    root.right.right=TreeNode(7)
    solver=Solutin()
    print(solver.level_order(root))