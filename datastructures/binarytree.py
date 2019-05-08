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

	def toList(self, mode:str='inorder') -> [int]:
		if mode not in [ 'inorder', 'preorder', 'postorder' ]:
			raise Exception('{0} is an invalid binary tree walk mode'.format(mode))

		valuelist = []
		if self.root is None:
			return valuelist

		if mode == 'inorder':
			BinarySearchTree.__toList_inorder(self.root, valuelist)
		elif mode == 'preorder':
			BinarySearchTree.__toList_preorder(self.root, valuelist)
		else:
			BinarySearchTree.__toList_postorder(self.root, valuelist)

		return valuelist

	@staticmethod
	def __toList_inorder(node: BinaryTreeNode, listptr: [int]):
		if node is not None:
			BinarySearchTree.__toList_inorder(node.left, listptr)
			listptr.append(node.value)
			BinarySearchTree.__toList_inorder(node.right, listptr)
		return

	@staticmethod
	def __toList_preorder(node: BinaryTreeNode, listptr: [int]):
		if node is not None:
			listptr.append(node.value)
			BinarySearchTree.__toList_preorder(node.left, listptr)
			BinarySearchTree.__toList_preorder(node.right, listptr)
		return

	@staticmethod
	def __toList_postorder(node: BinaryTreeNode, listptr: [int]):
		if node is not None:
			BinarySearchTree.__toList_postorder(node.left, listptr)
			BinarySearchTree.__toList_postorder(node.right, listptr)
			listptr.append(node.value)
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

	def delete(self, node: BinaryTreeNode):
		if node.left is None and node.right is None and node.parent is None:
			del node

		elif node.left is None and node.right is None:
			if node.value < node.parent.value:
				node.parent.left = None
			else:
				node.parent.right = None

			del node

		elif node.left is None or node.right is None:
			self.__del_one_subtree(node)

		else:
			self.__del_two_subtrees(node)

		return

	def __del_one_subtree(self, node: BinaryTreeNode):
		if node.right is None:
			if node.parent is None:
				self.root = node.left
			else:
				node.left.parent = node.parent
				if node.value < node.parent.value:
					node.parent.left = node.left
				else:
					node.parent.right = node.left

		else:
			if node.parent is None:
				self.root = node.right
			else:
				node.right.parent = node.parent
				if node.value < node.parent.value:
					node.parent.left = node.right
				else:
					node.parent.right = node.right
		del node
		return

	def __del_two_subtrees(self, node: BinaryTreeNode):
		successor = self.successor(node)
		node.value = successor.value
		self.delete(successor)
		return



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
	bst.insert(1)

	print('In-Order walk')
	print(bst.toList(mode='inorder'))

	print('\nPre-Order walk')
	print(bst.toList(mode='preorder'))

	print('\nPost-Order walk')
	print(bst.toList(mode='postorder'))
