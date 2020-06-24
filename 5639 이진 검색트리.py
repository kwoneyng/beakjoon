class Node:
	def __init__(self, key):
		self.key = key
		self.lchild = None
		self.rchild = None
	
class binarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, key):
		if self.root == None:
			self.root = Node(key)
		else:
			cur = self.root
			while True:
				if cur.key > key:
					if cur.lchild:
						cur = cur.lchild
					else:
						cur.lchild = Node(key)
						break
				elif cur.rchild:
					cur = cur.rchild
				else:
					cur.rchild = Node(key)
					break

	def preorder(self,node):
		s = []
		while True:
			try:
				print(node.key)
				if node.lchild:
					if node.rchild:
						s.append(node.rchild)
					node = node.lchild
				else:
					if node.rchild:
						s.append(node.rchild)
					node = s.pop()
			except:
				break

bst = binarySearchTree()
while True:
  try:
    key = int(input())
    bst.insert(key)
  except:
    break

bst.preorder(bst.root)




# class Node:
#   def __init__(self,key):
#     self.key = key
#     self.lchild = None
#     self.rchild = None
  
# class binarySearchTree:
#   def __init__(self):
#     self.root = None
#   def insert(self,key):
#     if self.root == None:
#       self.root = Node(key)
#     else:
#       current = self.root
#       while True:
#         if current.key > key:
#           if current.lchild == None:
#             current.lchild = Node(key)
#             break
#           current = current.lchild
#         if current.key < key:
#           if current.rchild == None:
#             current.rchild = Node(key)
#             break
#           current = current.rchild
#   def postorder(self, node):
#     s = []
#     while True:
#       while node:
#         if node.rchild:
#           s.append(node.rchild)
#         s.append(node)
#         node = node.lchild
#       node = s.pop()
#       if node.rchild and (s[-1] if len(s) else None) == node.rchild:
#         s.pop()
#         s.append(node)
#         node = node.rchild
#       else:
#         print(node.key)
#         node = None
#       if not s:
#         break

# bst = binarySearchTree()
# while True:
#   try:
#     key = int(input())
#     bst.insert(key)
#   except:
#     break

# bst.postorder(bst.root)