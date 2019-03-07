import unittest
from datastructures.binarytree import BinarySearchTree


class Test(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.values =       [ 12, 5, 2, 9, 18, 15, 13, 17, 19 ]
		cls.successors =   [ 13, 9, 5, 12, 19, 17, 15, 18, None ]
		cls.predecessors = [ 9, 2, None, 5, 17, 13, 12, 15, 18 ]
		cls.searchTree = BinarySearchTree()
		for v in cls.values:
			cls.searchTree.insert(v)
		return

	def testMinimum(self):
		node = self.searchTree.minimum()
		self.assertIsNotNone(node, msg='Minimum node does not exist')
		self.assertEqual(node.value, 2, msg='Incorrect tree-min')
		return

	def testMaximum(self):
		node = self.searchTree.maximum()
		self.assertIsNotNone(node, msg='Maximum node does not exist')
		self.assertEqual(node.value, 19, msg='Incorrect tree-max')
		return

	def testInOrderWalk(self):
		values = self.searchTree.toList(mode='inorder')
		self.assertEqual(values, [2, 5, 9, 12, 13, 15, 17, 18, 19], msg='Incorrect in-order walk')
		return

	def testPreOrderWalk(self):
		values = self.searchTree.toList(mode='preorder')
		self.assertEqual(values, [12, 5, 2, 9, 18, 15, 13, 17, 19], msg='Incorrect pre-order walk')
		return

	def testPostOrderWalk(self):
		values = self.searchTree.toList(mode='postorder')
		self.assertEqual(values, [2, 9, 5, 13, 17, 15, 19, 18, 12], msg='Incorrect post-order walk')
		return

	def testSearch(self):
		for v in self.values:
			node = self.searchTree.search(v)
			self.assertEqual(node.value, v, msg='Incorrect search value for v={0}: {1}'.format(v, node.value))
		return

	def testSuccessor(self):
		for i in range(len(self.values)):
			node = self.searchTree.search(self.values[i])
			successor = self.searchTree.successor(node)
			if successor is None:
				self.assertIsNone(self.successors[i])
			else:
				self.assertEqual(successor.value, self.successors[i], msg='Incorrect successor for node {0}: {1}'.format(node.value, successor.value))
		return

	def testPredecessor(self):
		for i in range(len(self.values)):
			node = self.searchTree.search(self.values[i])
			predecessor = self.searchTree.predecessor(node)
			if predecessor is None:
				self.assertIsNone(self.predecessors[i])
			else:
				self.assertEqual(predecessor.value, self.predecessors[i], msg='Incorrect predecessor for node {0}: {1}'.format(node.value, predecessor.value))
		return