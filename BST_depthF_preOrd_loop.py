# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:36:40 2020

Binary search tree: depth first search, preorder traversal

@author: smorarka
"""

class Node(object):
    """ This is a node object that has value attribute and left and right nodes"""
    def __init__(self, element):
        self.value = element
        self.left = None
        self.right = None


class BST(object):
    """ This is binary search tree class. Contains root node and other functions"""
    def __init__(self, rootEle):
        self.root = Node(rootEle)


tree=BST(4)
tree.insert(5)
#tree.insert(6)
#tree.insert(1)
#tree.insert(2)
#tree.insert(1.5)
#tree.print_tree()
##print(tree.search(1.5))
#tree.delete(1.5)
##tree.print_tree()