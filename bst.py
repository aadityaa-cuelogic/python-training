import sys
# Define TREE class
class Tree:
    # init method - constuctor in python
    def __init__(self, Node=None):
        self.left = None
        self.right = None
        self.root = Node

    def insertNode(self, Node):
        if self.root:
            #insert left or right child Node
            if Node < self.root:
                if self.left == None:
                    self.left = Tree(Node)
                else:
                    self.left.insertNode(Node)
            elif Node > self.root:
                if Node > self.right:
                    if self.right == None:
                        self.right = Tree(Node)
                    else:
                        self.right.insertNode(Node)
        else:
            self.root = Node #insert new root

    def printTree(self, Node=None):
        # Pre order traversal
        print self.root, "\n",
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

        # # In order traversal
        # if self.left:
        #     self.printTree()
        # print self.root, "\n",
        # if self.right:
        #     self.right.printTree()

        # # Post order traversal
        # if self.left:
        #     self.left.printTree()
        # if self.right:
        #     self.right.printTree()
        # print self.root



    def searchTreeNode(self, Node):
        if Node < self.root:
            if self.left == None:
                print "Node does not exists!!!"
                exit(0)
            return self.left.searchTreeNode(Node)
        elif Node > self.root:
            if self.right == None:
                print "Node does not exists!!!"
                exit(0)
            return self.right.searchTreeNode(Node)
        else:
            print "FOUND: ",self.root



#Create Tree instance
myTree = Tree()
# myTree.printTree()
myTree.insertNode(20)
myTree.insertNode(17)
myTree.insertNode(18)
myTree.insertNode(25)
myTree.insertNode(23)
myTree.insertNode(24)
myTree.printTree()
print "Find 17 :\n"
myTree.searchTreeNode(17)
