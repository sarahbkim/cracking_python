#!/usr/bin/python
from collections import deque
import unittest
from decimal import Decimal

class BinaryTree():
    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, value):
        self.rootid = value

    def getNodeValue(self):
        return self.rootid

    def insertLeftChild(self, value):
        if self.left == None:
            self.left = BinaryTree(value)

    def insertRightChild(self, value):
        if self.right == None:
            self.right = BinaryTree(value)

    def pre_order(self):
        items = []
        items.append(self.getNodeValue())
        if self.getLeftChild() != None:
            items.append(self.getLeftChild().pre_order())
        if self.right != None:
            items.append(self.getRightChild().pre_order())
        return items

    def in_order(self):
        items = []
        if self.getLeftChild() != None:
            items.append(self.getLeftChild().in_order())
        items.append(self.getNodeValue())
        if self.getRightChild() != None:
            items.append(self.getRightChild().in_order())
        return items

    def post_order(self):
        items = []
        if self.getLeftChild() != None:
            items.append(self.getLeftChild().post_order())
        if self.getRightChild() != None:
            items.append(self.getRightChild().post_order())
        items.append(self.getNodeValue())
        return items

    # to know what level i am at, i can keep a current count of 
    # nodes passed 
    # and increment counts of nodes i'm adding
    # if my current count is back to zero, then I am passed that level
    def level_order(self):
        items = []
        queue = deque()
        items.append([self.getNodeValue()])
        queue.append(self)

        level = 1
        current_count = 1
        node_count = 0
        level_arr = []

        while queue:
            current = queue.popleft()
            current_count -= 1
            if current.getLeftChild() != None:
                queue.append(current.getLeftChild())
                node_count += 1
                level_arr.append(current.getLeftChild().getNodeValue())
            if current.getRightChild() != None:
                queue.append(current.getRightChild())
                node_count += 1
                level_arr.append(current.getRightChild().getNodeValue())
            if current_count == 0:
                items.append(level_arr)
                level += 1
                level_arr = []
                current_count = node_count
        return items

    def reverse_level_order(self):
        items = {}
        items[0] = [self.getNodeValue()]
        queue = deque()
        queue.append(self)
        level = 1
        current_count = 1
        node_count = 0
        level_arr = []

        while queue:
            current = queue.popleft()
            current_count -= 1
            if current.getLeftChild() != None:
                queue.append(current.getLeftChild())
                node_count += 1
                level_arr.append(current.getLeftChild().getNodeValue())
            if current.getRightChild() != None:
                queue.append(current.getRightChild())
                node_count += 1
                level_arr.append(current.getRightChild().getNodeValue())

            if current_count == 0:
                items[level] = level_arr
                level += 1
                level_arr = []
                current_count = node_count
        
        start = len(items.keys())-1
        answer = []
        while start>=0:
            answer.append(items[start])
            start -= 1
        return answer


    def print_list_vals(self, arr):
        string = ''
        for i in arr:
            string += str(i.getNodeValue()) + ' '
        return string

    def breadth_first_test(self):
        queue = [self]
        while len(queue)!=0:
            for current in queue:
                temp = []
                if current.getLeftChild() != None: temp.append(current.getLeftChild())
                if current.getRightChild() != None: temp.append(current.getRightChild())
            queue = temp

    # need to use a queue, and is not a recursive implementation
    def breadth_first(self):
        queue = [self]

        while len(queue)!=0:
            for n in queue:
                nextLevel = []
                if n.getLeftChild() != None: nextLevel.append(n.getLeftChild())
                if n.getRightChild() != None: nextLevel.append(n.getRightChild())
            queue = nextLevel



'''
Given the root of a binary search tree and 2 numbers min and max, 
trim the tree such that all the numbers in the new tree are between min 
and max (inclusive). The resulting tree should still be a valid binary 
search tree.

do a post-order traversal 

assumes that the tree is a valid binary search tree! 
'''
def trim(tree, minV, maxV):
    if not tree:
        return

    if tree.getLeftChild():
        trim(tree.getLeftChild(), minV, maxV)
    if tree.getRightChild():
        trim(tree.getRightChild(), minV, maxV)

    items = []
    if minV <= tree.getNodeValue() <= maxV:
        items.append(tree.getNodeValue())
        return items
    if tree.getNodeValue() < minV:
        return tree.getRightChild()
    if tree.getNodeValue() > maxV:
        return tree.getLeftChild()

def check_binary_search(tree, lastNode=Decimal('-Infinity')):
    if tree is None:
        return True
    
    if not check_binary_search(tree.getLeftChild(), lastNode):
        return False
    print tree.getNodeValue(), lastNode
    if tree.getNodeValue() < lastNode:
        return False

    lastNode = tree.getNodeValue()
    
    return check_binary_search(tree.getRightChild(), lastNode)


class binary_search_test(unittest.TestCase):
    def test_check_b(self):
        # tree = BinaryTree(8)
        # tree.insertLeftChild(3)
        # tree.insertRightChild(10)
        # tree.getLeftChild().insertLeftChild(1)
        # tree.getLeftChild().insertRightChild(6)
        # tree.getRightChild().insertLeftChild(14)
        # tree.getRightChild().getLeftChild().insertLeftChild(13)
        # tree.getLeftChild().getLeftChild().insertLeftChild(4)
        # tree.getLeftChild().getLeftChild().insertRightChild(7)
        
        # self.assertEquals(check_binary_search(tree), True)

        tree2 = BinaryTree(8)
        tree2.insertLeftChild(1)
        tree2.insertRightChild(20)
        self.assertEquals(check_binary_search(tree2), False)

    # def test_trim(self):
    #     tree = BinaryTree(8)
    #     tree.insertLeftChild(3)
    #     tree.insertRightChild(10)
    #     tree.getLeftChild().insertLeftChild(1)
    #     tree.getLeftChild().insertRightChild(6)
    #     tree.getRightChild().insertLeftChild(14)
    #     tree.getRightChild().getLeftChild().insertLeftChild(13)
    #     tree.getLeftChild().getLeftChild().insertLeftChild(4)
    #     tree.getLeftChild().getLeftChild().insertRightChild(7)
        
    #     x = trim(tree, 6, 12)

    #     self.assertEquals( x, [3, 8, 10])


    def test_reverse_level_order(self):
        tree = BinaryTree(1)
        tree.insertLeftChild(2)
        tree.insertRightChild(3)
        tree.getLeftChild().insertLeftChild(4)
        tree.getRightChild().insertLeftChild(5)
        tree.getRightChild().insertRightChild(6)
        x = tree.reverse_level_order()
        self.assertEquals(x, [[4, 5, 6], [2, 3], [1]])

    def test_instantiate_binary_tree(self):
        # make sure instantiation of binary tree works
        tree = BinaryTree(10)
        tree.insertRightChild(3)
        tree.insertLeftChild(7)
        
        self.assertEquals(tree.getLeftChild().getNodeValue(), 7)
        self.assertEquals(tree.getRightChild().getNodeValue(), 3)
        
        tree.insertLeftChild(10)
        self.assertEquals(tree.getLeftChild().getNodeValue(), 7)

        tree.getLeftChild().insertRightChild(4)
        self.assertEquals(tree.getLeftChild().getRightChild().getNodeValue(), 4)

    def test_pre_order(self):
        tree = BinaryTree(10)
        tree.insertRightChild(3)
        tree.insertLeftChild(7)
        tree.getLeftChild().insertRightChild(4)
        tree.getLeftChild().insertLeftChild(1)
        tree.getRightChild().insertRightChild(8)
        tree.getRightChild().insertLeftChild(5)
        x = tree.pre_order()
        self.assertEquals(x, [10, [7, [1], [4]], [3, [5], [8]]])

    def test_level_order(self):
        tree = BinaryTree(1)
        tree.insertLeftChild(2)
        tree.insertRightChild(3)
        tree.getLeftChild().insertLeftChild(4)
        tree.getRightChild().insertLeftChild(5)
        tree.getRightChild().insertRightChild(6)
        x = tree.level_order()
        self.assertEquals(x, [[1],[2,3],[4,5,6]])

    def test_in_order(self):
        tree = BinaryTree(10)
        tree.insertRightChild(3)
        tree.insertLeftChild(7)
        tree.getLeftChild().insertRightChild(4)
        tree.getLeftChild().insertLeftChild(1)
        tree.getRightChild().insertRightChild(8)
        tree.getRightChild().insertLeftChild(5)

        y = tree.in_order()
        self.assertEquals(y, [[[1], 7, [4]], 10, [[5], 3, [8]]])

    def test_post_order(self):
        tree = BinaryTree(10)
        tree.insertRightChild(3)
        tree.insertLeftChild(7)
        tree.getLeftChild().insertRightChild(4)
        tree.getLeftChild().insertLeftChild(1)
        tree.getRightChild().insertRightChild(8)
        tree.getRightChild().insertLeftChild(5)

        x = tree.post_order()
        self.assertEquals(x, [[[1], [4], 7], [[5], [8], 3], 10])

    def test_breadth_first(self):
        tree = BinaryTree(10)
        tree.insertRightChild(3)
        tree.insertLeftChild(7)
        tree.getLeftChild().insertRightChild(4)
        tree.getLeftChild().insertLeftChild(1)
        tree.getRightChild().insertRightChild(8)
        tree.getRightChild().insertLeftChild(5)

        x = tree.breadth_first_test()


if __name__ == '__main__':
    unittest.main()