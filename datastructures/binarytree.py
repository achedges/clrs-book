class BinaryTreeNode:
	def __init__(self):
		self.parent: BinaryTreeNode = None
		self.left: BinaryTreeNode = None
		self.right: BinaryTreeNode = None
		self.value: int = None

	def __str__(self):
		return 'null' if self.value is None else str(self.value)



class BinarySearchTree:

	def __init__(self):
		self.root: BinaryTreeNode = None

	def walk(self, mode:str='inorder') -> BinaryTreeNode:
		if mode not in [ 'inorder', 'preorder', 'postorder' ]:
			raise Exception('{0} is an invalid binary tree walk mode'.format(mode))

		if self.root is None:
			return BinaryTreeNode()

		if mode == 'inorder':
			BinarySearchTree.__walk_inorder(self.root)
		elif mode == 'preorder':
			BinarySearchTree.__walk_preorder(self.root)
		else:
			BinarySearchTree.__walk_postorder(self.root)

	@staticmethod
	def __walk_inorder(node):
		if node is not None:
			BinarySearchTree.__walk_inorder(node.left)
			print(node.value)
			BinarySearchTree.__walk_inorder(node.right)
		return

	@staticmethod
	def __walk_preorder(node):
		if node is not None:
			print(node.value)
			BinarySearchTree.__walk_preorder(node.left)
			BinarySearchTree.__walk_preorder(node.right)
		return

	@staticmethod
	def __walk_postorder(node):
		if node is not None:
			BinarySearchTree.__walk_postorder(node.left)
			BinarySearchTree.__walk_postorder(node.right)
			print(node.value)
		return

	def search(self, value: int) -> BinaryTreeNode:
		node = self.root
		while node.value is not None and node.value != value:
			node = node.left if value < node.value else node.right
		return node

	def minimum(self, subtree: BinaryTreeNode = None) -> BinaryTreeNode:
		if subtree is None: subtree = self.root
		while subtree.left is not None:
			subtree = subtree.left
		return subtree

	def maximum(self, subtree: BinaryTreeNode = None) -> BinaryTreeNode:
		if subtree is None: subtree = self.root
		while subtree.right is not None:
			subtree = subtree.right
		return subtree

	def successor(self, node: BinaryTreeNode) -> BinaryTreeNode:
		if node.right is not None:
			return self.minimum(node.right)

		_parent = node.parent
		while _parent is not None and node.value == _parent.right.value:
			node = _parent
			_parent = _parent.parent

		return _parent

	def predecessor(self, node: BinaryTreeNode) -> BinaryTreeNode:
		if node.left is not None:
			return self.maximum(node.left)

		_parent = node.parent
		while _parent is not None and node.value == _parent.left.value:
			node = _parent
			_parent = _parent.parent

		return _parent

	def insert(self, value: int) -> BinaryTreeNode:
		new = BinaryTreeNode()
		new.value = value

		if self.root is None:
			self.root = new
			return new

		node = self.root
		while node is not None:
			new.parent = node
			if new.value < node.value:
				node = node.left
			else:
				node = node.right

		if new.value < new.parent.value:
			new.parent.left = new
		else:
			new.parent.right = new

		return new



if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.insert(12)
	bst.insert(5)
	bst.insert(2)
	bst.insert(9)
	bst.insert(18)
	bst.insert(15)
	bst.insert(13)
	bst.insert(17)
	bst.insert(19)

	print('In-Order walk')
	bst.walk(mode='inorder')

	print('\nPre-Order walk')
	bst.walk(mode='preorder')

	print('\nPost-Order walk')
	bst.walk(mode='postorder')
