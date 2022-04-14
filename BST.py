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

class Node(object):
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
class BinaryTree(object):
    def __init__(self):
        self.node = None

    # # left, root, right
    # def inOrderTraversal(self):
    #     # base case
    #     if self.node == None:
    #         print("binary tree is empty. Nothing to traverse.")
    #         return
    #     BT_arr = []
    #     itr = self.node
    #     # iterate through left
    #     while itr:
    #         BT_arr.append(itr)
    #         itr = itr.left
    #         break
        
    
    def printBinaryTree(self):
        if self.node is None:
            print("Binary tree is empty")
            return
        BTstr = ''
        itr = self.node
        while itr:
            BTstr += str(itr.data) + "->" 
            itr = itr.left
        print(BTstr)

    # insert from head of list
    def insert(self, item):
        if self.node is None:
            currentNode = Node(item)
            self.node(currentNode)

        # binary tree is not empty
        # iterate to the leaf node, then determine whether it's a right or left node
        # parent = self.node.data
        # if item < parent:
        #     print("less than parent, go to left")
        # elif item > parent:
        #     print("greater than parent")
        # else:
        #     print("node is duplicate and cannot be added.")
        

if __name__ == '__main__':
    BT = BinaryTree()
    BT.insert(5)
    BT.printBinaryTree()
            
        

