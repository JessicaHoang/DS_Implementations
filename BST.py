'''
Goal: Implement a binary search tree with 
a Node class and BinaryTree class

function: append: how do I add nodes, where do I add nodes?
append: create a new node and give it the correct reference.
- if node == root, then create it and give it the index 0
- otherwise compare the node to see 


'''
# from numpy import left_shift

# node_arr = []
# # 1
# class Node(object):
#     # Node has a key and data.
#     # access the node's data with the node's key
#     def __init__(self):
#         self.node = None
#         self.parent = None
#         self.left = None
#         self.right = None
#         self.root = None

#     def addNode(self, node):
#         # base case: array is empty, so append
#         try:
#             node_arr.append(node)
#         except:
#             print("unable to add node.")
    
# # 2
# class BinaryTree(object):
#     def __init__(self):
#         self.node = None
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.depth = None
    
#     # when inserting into the tree, keep track of the depth
#     def insertNode(self, node):
#             # adding node to tree
#             # base case: array is empty, so append
#         try:
#             if len(node_arr) == 0:
#                 self.parent = node # for the children nodes
#                 self.root = node # this node is still the root node
#                 node_arr.append(node)
#                 print(node, " is the root")
#             # adding nodes to a non-empty array
#             elif len(node_arr) >= 1:
#                 if node < self.root:
#                     print(node, " has been added as left child of ", self.parent)
#                     self.left = node
#                     node_arr.append(node)
#                 else:
#                     print(node, " has been added as right child of ", self.parent)
#                     self.right = node
#                     node_arr.append(node)
#         except:
#             print("unable to add node to tree")
    
# tree = BinaryTree()
# tree.insertNode(56)
# tree.insertNode(23)
# tree.insertNode(67)
# tree.insertNode(83)

# from logging import root


# BT = []

# class Node(object):

#     def __init__(self, data = None):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __repr__(self):
#         return self.data

# # 3
# class BinaryTree(object):

#     def __init__(self, iter = []):
#         self.node = None
#         self.size = 0
#         for item in iter:
#             self.append(item)
    
#     def append(self, item):
#         # create a node
#         node = Node()
#         node.data = item
#         # base case: first node in the BT
#         if

    
#     def get_leaf_node(self, node):
#         # search through all nodes and return the lead node
#         try:
#             if Node.left == None and Node.right == None:
#                 return node
#         except:
#             print("unable to run get_leaf_node function")
        
# # 4
# class Node(object):

#     def __init__(self, data = None):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __repr__(self):
#         return self.data


# class BinaryTree(object):

#     # def __init__(self, root=None):
#     #     self.root = Node(root)
#     def __init__(self, iter = []):
#         self.root = None
#         self.node = None
#         for item in iter:
#             self.append(item)
    
#     def append(self, item):
#         # base case: first node in the BT
#         if self.root == None:
#             self.root = Node(item)
#             print(Node(item), " is root")
#             return self.root
#         else:
#             print("can't add")
#             self.appendNonRoot(item)
#             return
    
#     # problem with this function is not knowing what to compare 
#     # item to.
#     def appendNonRoot(self, item):
#         # check if it's the leaf node
#         current = self.root
#         # append when it's less than the parent
#         if (item < current.data):
#             if not current.left:
#                 current.left = Node(item)
#                 current = current.left
#         # append when it's greater than the parent
#         else:
#             if not current.right:
#                 current.right = Node(item)
#                 current = current.right
    
#     # implement search

#     # implement delete
        
    
# tree = BinaryTree()
# print(tree.append(45))
# print(tree.append(36))

# # finding the leaf nodes
#             if node.left == None and node.right == None: 
#                 if item < node.data:
#                     print("insert into right tree")
#                     node.right = item
#                     return node.right
#                 elif item > node.data:
#                     print("insert into left")
#                     node.left = item
#                     return node.left
#                 else:
#                     return

# # 5
# class BinaryTree(object):
#     def __init__(self, data = None, key = None):
#         self.data = data
#         self.key = key
#         self.left = None
#         self.right = None
#         self.root = None

#     # print/return out the data
#     def __repr__(self, data):
#         self.data = data
#         return self.data

#     def append(self, data):
#         # base case: if there were no nodes
#         if self.root == None:
#             key = 0 # first key
#             return self.__repr__(self.root)
#         # this is not the first node in the function
#         else:
#             self.appendNonRoot(data)
    
#     def appendNonRoot(self, data):
#         # comparing data with current nodes in the binary tree
#         latestNode = self.root
#         # appending left means left has to be vacant
    
#     def searchBT(self, key):
#         # check if tree is empty
#         if self.root == None:
#             print("Binary Tree is empty.")
#         # check if tree is not empty
#         else:

from hashlib import new


class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree(object):
    def __init__(self, node = None):
        self.node = node
    
    def inOrderTraversal(self):
        # newNode = Node(newNodeData)
        elements = []
        # visit left tree
        if self.node.left:
            elements += self.inOrderTraversal()
        # visit base node
        elements.append(self.node.data)
        # visit right tree
        if self.node.right:
            elements += self.inOrderTraversal()
        return elements
    
    def printBinaryTree(self):
        # # root is the first node
        # root = BinaryTree(elements[0])
        # root.insert(elements[0])
        # # iterate through element list and insert node into it
        # for i in range(1, len(elements)):
        #     root.insertNonRoot(elements[i])
        #     # print(root.insertNonRoot(elements[i]))
        
        # return root
        
        if self.node is None:
            print("Binary tree is empty")
            return
        BTstr = ''
        while self.node.data in self.inOrderTraversal():
            BTstr += str(self.node.data)
        print(BTstr)

        # if self.node is None:
        #     print("Binary tree is empty")
        #     return
        # BTstr = ''
        # itr = self.node
        # while itr:
        #     BTstr += str(itr.data) + "-->"
        #     itr = itr.left
        # print(BTstr)

    # insert from head of list
    def insert(self, item):
        node = Node(item)
        self.node = node

    def insertNonRoot(self, newNodeData):
        newNode = Node(newNodeData)
        # do not inser duplicates
        if newNode.data == self.node.data:
            return
        # insert in left
        if newNode.data < self.node.data:
            if self.node.left:
                print("node is less than parent node")
                self.insertNonRoot(newNode.data)
                # newNode.left = None
                # newNode.right = None
            else:
                self.node.data = newNode.data
                newNode.left = None
                newNode.right = None
        # insert in right
        else:
            if self.node.right:
                print("node is more than parent node")
                self.insertNonRoot(newNode.data)
                # newNode.left = None
                # newNode.right = None
            else:
                self.node.data = newNode.data
                newNode.left = None
                newNode.right = None

if __name__ == '__main__':
    BT = BinaryTree()
    # BT.insert(60)
    # BT.insertNonRoot(62)
    # BT.insertNonRoot(34)
    # BT.insertNonRoot(58)
    # BT.insertNonRoot(87)
    element_list = [60,62, 34, 58, 87]
    elements_tree = BT.printBinaryTree()
    print(BT.inOrderTraversal())
    BT.printBinaryTree()
            
        

