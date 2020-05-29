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
        """insert an element in the BST"""
        self.insert_helper(self.root, element)
        return
    
    def insert_helper(self, start, new_element):
        """insert helper function for inserting element in BST"""
#        print(start.value, new_element)
        if new_element < start.value:
            if start.left:
                return self.insert_helper(start.left, new_element)
            else:
                start.left = Node(new_element)
                return
        else:
            if start.right:
                return self.insert_helper(start.right, new_element)
            else:
                start.right = Node(new_element)
                return

    def delete(self, del_val):
        """ this function deletes the del_val from tree if exists and rearranges the tree if needed"""
        list = []
        return self.delete_helper(self.root, del_val, list)

    def delete_helper(self, start, del_val, list):
        """find the element and delete"""
        if start.value == del_val:
            parent = list[-1]
            kid = start
            kid_is_left = 1 if parent.left == kid else 0
            if not kid.left and not kid.right:
                if kid_is_left: 
                    parent.left = None
                else:
                    parent.right = None
            
            return 1
        elif (del_val < start.value and not start.left) or (del_val > start.value and not start.right):
            return 0
        elif del_val < start.value:
            list.append(start)
            return self.delete_helper(start.left, del_val, list)
        else:
            list.append(start)
            return self.delete_helper(start.right, del_val, list)
    
    def search(self, find_val):
        """return 1 if found and -1 if not"""
        return (self.search_helper(self.root, find_val)[1])
       
    def search_helper(self, start, find_val):
        if start.value == find_val:
            return 1
        elif (find_val < start.value and not start.left) or (find_val > start.value and not start.right):
            return 0
        elif find_val < start.value:
            return self.search_helper(start.left, find_val)
        else:
            return self.search_helper(start.right, find_val)
        
    def print_tree(self):
        """prints the tree"""
        traverse = []
        self.print_helper(self.root, traverse)
        sep = '-'*len(traverse)
        print(''.join(traverse)[:-1])
    
    def print_helper(self, start, traverse):
        """print tree's helper function"""
        traverse.append(str(start.value)+'-')
        if start.left:
            self.print_helper(start.left, traverse)
        if start.right:
            self.print_helper(start.right, traverse)


tree=BST(4)
tree.insert(5)
tree.insert(6)
tree.insert(1)
tree.insert(2)
tree.insert(1.5)
tree.print_tree()
#print(tree.search(1.5))
tree.delete(1.5)
#tree.print_tree()