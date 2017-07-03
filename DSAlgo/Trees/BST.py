
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue():
    def __init__(self) :
        self.level_order_queue = []        

    def enqueue(self, levelnode) :
        self.level_order_queue.append(levelnode)

    def dequeue(self) :
        if len(self.level_order_queue) > 0 :
            return self.level_order_queue.pop(0)
        else :
            return None

class BST():
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, data, curr_node):
        if curr_node.data > data :
            if curr_node.left == None :
                curr_node.left = Node(data)
                print "Inserting {0} to the left of {1}".format(curr_node.left.data, curr_node.data)
            else :
                self.insertNode(data, curr_node.left)
        else :
            if curr_node.right == None :
                curr_node.right = Node(data)
                print "Inserting {0} to the right of {1}".format(curr_node.right.data, curr_node.data)
            else :
                self.insertNode(data, curr_node.right)
    
    def PreOrderTraversal(self, present_root) :
        if not present_root :
            return
        print present_root.data
        self.PreOrderTraversal(present_root.left)
        self.PreOrderTraversal(present_root.right)
            
    def InOrderTraversal(self, present_root) :
        if present_root :
            self.InOrderTraversal(present_root.left)
            print present_root.data
            self.InOrderTraversal(present_root.right)
        else :
            return

    def PostOrderTraversal(self, present_root) :
        if not present_root :
            return
        self.PostOrderTraversal(present_root.left)
        self.PostOrderTraversal(present_root.right)
        print present_root.data

    def LevelOrderTraversal(self) :
        queue_obj = Queue()
        temp_node = self.root
        while temp_node :
            print temp_node.data
            if temp_node.left :
                queue_obj.enqueue(temp_node.left)
            if temp_node.right :
                queue_obj.enqueue(temp_node.right)
            temp_node = queue_obj.dequeue()

    def GetTreeHeight(self, present_root):
        if present_root :
            lheight = self.GetTreeHeight(present_root.left)
            rheight = self.GetTreeHeight(present_root.right)
            print lheight,rheight
            if lheight > rheight :
                return lheight + 1
            else :
                return rheight + 1
        else :
            return 0     

if __name__ == "__main__" :
    bst_obj = BST(5)
    for i in [1,3,8,6,4,2] :
    #for i in [5,2,3,1] :
        bst_obj.insertNode(i, bst_obj.root) 
    print "Pre-Order Traversal"
    bst_obj.PreOrderTraversal(bst_obj.root)
    print "In-Order Traversal"
    bst_obj.InOrderTraversal(bst_obj.root)
    print "Post-Order Traversal"
    bst_obj.PostOrderTraversal(bst_obj.root)
    print "Level Order Traversal"
    bst_obj.LevelOrderTraversal()
    tree_height = bst_obj.GetTreeHeight(bst_obj.root)
    print "Height of the given binary tree is {0}".format(tree_height)
