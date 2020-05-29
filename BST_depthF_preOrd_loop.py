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

    def insert(self, element):
        if self.root:
            start = self.root
            list = [start]
            for node in list:
                if (element < node.value and node.left) or element > node.value and node.right:
                    list.append(node.left if element < node.value else node.right)
                elif element < node.value and not node.left:
                    node.left = Node(element)
                else:
                    node.right = Node(element)
        else:
            self.root = Node(element)

    def print_tree(self):
        if self.root:
            start = self.root
            list = [start]
            for node in list:
                print(node.value)
                if node.left:
                    list.append(node.left)
                elif node.right:
                    list.append(node.right)
                else:
#                    for i in reversed(list[:-1]):
#                        print([a.value for a in list])
#                        print(node.value)
#                        if node.left:
#                            list.append(node.left)
#                        elif node.right:
#                            list.append(node.right)
#                        else:
#                            print("do nothing")
        else:
            print("can't find root")
        return
    
tree=BST(4)
tree.insert(5)
tree.insert(6)
tree.insert(1)
tree.insert(0.8)
tree.insert(2)
tree.insert(1.5)
tree.print_tree()
##print(tree.search(1.5))
#tree.delete(1.5)
##tree.print_tree()