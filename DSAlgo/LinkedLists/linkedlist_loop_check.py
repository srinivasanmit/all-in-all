
class Node() :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList() :
    def __init__(self):
        self.head = None
        self.tail = None
        self.ll_length = 0

    def appendNode(self, data) :
        new_node = Node(data)
        if not self.head :
            self.head = new_node
        else :
            curr_node = self.head
            while curr_node.next :
                curr_node = curr_node.next
            curr_node.next = new_node
            self.tail = new_node

    def create_loop(self) :
        self.tail.next = self.head

    def check_for_loops(self) :
        hop1 = hop2 = self.head
        while hop1 :
            hop1 = hop1.next
            hop2 = hop2.next.next
            if hop1 == hop2 :
                print "Loop detected"
                break
        else :
            print "Loop not detected"

if __name__ == "__main__" :
    ll_obj = LinkedList()
    print "Appending 1 to list"
    ll_obj.appendNode(1)
    print "Appending 2 to list"
    ll_obj.appendNode(2)
    print "Appending 3 to list"
    ll_obj.appendNode(3)
    print "Appending 4 to list"
    ll_obj.appendNode(4)
    print "Appending 5 to list"
    ll_obj.appendNode(5)
    ll_obj.create_loop()
    print "Checking for loops........"
    ll_obj.check_for_loops()

