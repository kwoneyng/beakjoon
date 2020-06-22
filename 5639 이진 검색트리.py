class Node:
  def __init__(self,key):
    self.key = key
    self.lchild = None
    self.rchild = None
  
class binarySearchTree:
  def __init__(self):
    self.root = None
  def insert(self,key):
    if self.root == None:
      self.root = Node(key)
    else:
      current = self.root
      while True:
        if current.key > key:
          if current.lchild == None:
            current.lchild = Node(key)
            break
          current = current.lchild
        if current.key < key:
          if current.rchild == None:
            current.rchild = Node(key)
            break
          current = current.rchild
  def postorder(self, node):
    s = []
    while True:
      while node.lchild:
        node = node.lchild
        s.append(node.key)
      print(node.key)
      node = s.pop()
      print(node.key)
      if node.rchild:
        

bst = binarySearchTree()
while True:
  try:
    key = int(input())
    bst.insert(key)
  except:
    break

print("ad")
# bst.postorder(bst.root)