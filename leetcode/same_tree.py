class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def insert(self, data):
    if self.val == 0:
      self.val = data
    elif self.left is None or self.right is None:
        if self.left is None:
          self.left= TreeNode(data) 
        else: self.right = TreeNode(data)
    else:
      # this doesn't work as intended. But what is intended really??
        self.right.insert(data)

class Solution:
  def is_same_tree(self, p, q) -> bool:
    if p is None and q is None:
      return True
    if p is None or q is None:
      return False
    if p.val != q.val:
      return False
    return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
  
  def traverse(self, rootNode):
    cache = []
    if rootNode.left:
      cache.append(self.traverse(rootNode.left))
    cache.append(rootNode.val)
    if rootNode.right:
      cache.append(self.traverse(rootNode.right))
    return (cache)
  def is_(self, p, q):
    r1 = self.traverse(q)
    r2 = self.traverse(p)
    return r1 == r2

p = TreeNode()
p.insert(1)
p.insert(2)

q = TreeNode()
q.insert(1)
q.insert('null')
q.insert(2)

s = Solution()
print(s.is_(p, q))
print(s.is_same_tree(p,q))