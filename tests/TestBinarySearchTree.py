import unittest
from datastructures.binarytree import BinarySearchTree


class Test(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.values = [ 12, 5, 2, 9, 18, 15, 13, 17, 19 ]
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

	def testSearch(self):
		for v in self.values:
			node = self.searchTree.search(v)
			self.assertEqual(node.value, v, msg='Incorrect search value for v={0}: {1}'.format(v, node.value))
		return

	def testSuccessor(self):
		node = self.searchTree.search(9)
		successor = self.searchTree.successor(node) # should be 12
		self.assertEqual(successor.value, 12, msg='Incorrect successor for node {0}: {1}'.format(node.value, successor.value))
		return

	def testPredecessor(self):
		node = self.searchTree.search(15)
		predecessor = self.searchTree.predecessor(node) # should be 13
		self.assertEqual(predecessor.value, 13, msg='Incorrect predecessor for node {0}: {1}'.format(node.value, predecessor.value))
		return