import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree() :
    def __init__(self):
        self.root = Node(4)
        self.printed_val = - sys.maxint -1

    def bst_or_not(self, present_root) :
        if present_root :
            self.bst_or_not(present_root.left)
            if not self.printed_val < present_root.data :
                print "Given Tree is not a BST"
                sys.exit(0)
            self.printed_val = present_root.data
            print present_root.data
            self.bst_or_not(present_root.right)
        else :
            return

if __name__ == "__main__" :
    tree_root = Tree()
    tree_root.root.left = Node(2)
    tree_root.root.left.left = Node(1)
    tree_root.root.left.right = Node(3)
    tree_root.root.right = Node(5)
    tree_root.bst_or_not(tree_root.root)
    print "Given tree is a BST"
