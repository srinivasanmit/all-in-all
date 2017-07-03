
class Node() :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList() :
    def __init__(self):
        self.head = None
        self.tail = None
        self.ll_length = 0
    
    def appendNode(self, data):
        new_node = Node(data)
        self.ll_length += 1
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node

    def insertNode(self, data, position) :
        new_node = Node(data)
        curr_node = self.head
        i = 1
        self.ll_length += 1
        if position > self.ll_length :
            print "Position can't be greater than the length of LL"
        elif position != 1 :
            while i < position -1 :
                curr_node = curr_node.next
                i += 1
            new_node.next = curr_node.next
            curr_node.next = new_node
        else :
            new_node.next = curr_node
            self.head = new_node

    def insert_into_sorted(self, data) :
        new_node = Node(data)
        self.ll_length += 1
        curr_node = self.head
        print "inserting ", data
        while curr_node.next != None :
            if data < self.head.data :
                new_node.next = self.head
                self.head = new_node
                break
            elif data > curr_node.data and data < curr_node.next.data :
                new_node.next = curr_node.next 
                curr_node.next = new_node
                break
            elif data > curr_node.next.data :
                curr_node.next.next = new_node
            curr_node = curr_node.next
        if data > self.head.data :
            self.head.next = new_node
        else :
            new_node.next = self.head
            self.head = new_node 
                    

    def deleteNode(self, data):
        curr_node = self.head
        prev_node = self.head 
        if self.head.data == data :
            self.head = self.head.next
            self.ll_length -= 1
            return

        while curr_node.next != None :
            if curr_node.data == data :
                prev_node.next = curr_node.next
                del(curr_node)
                self.ll_length -= 1
                break
            prev_node = curr_node
            curr_node = curr_node.next
            
        else :
            print "Could not find item to delete in the linked list"
    
    def reverseList(self):
        tmp_curr_node = curr_node = self.head
        prev_node = None
        revList = LinkedList()
        while curr_node :
            tmp_current_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            revList.appendNode(curr_node.data)
            curr_node = tmp_current_node
        self.head = prev_node
        return revList
    
    def printNodes(self) :
        curr_node = self.head
        while curr_node != None :
            print curr_node.data
            curr_node = curr_node.next

    def getLength(self, head_pointer) :
        count = 0
        while head_pointer :
            count += 1
            head_pointer = head_pointer.next
        return count

    def checkPalindromeLists(self, revobj ) :
        curr_node = self.head
        rev_curr_node = revobj.head
        if self.getLength(self.head) != self.getLength(revobj.head) :
            print "Linked lists are not palidromes"
        while curr_node :
            if curr_node.data != rev_curr_node.data :
                return False
            curr_node = curr_node.next
            rev_curr_node = rev_curr_node.next
        else :
            return True

if __name__ == "__main__":
    ll_obj = LinkedList()
    print "Appending 1 to the linked list"
    ll_obj.appendNode(1)
    ll_obj.printNodes()
    print "Appending 3 to the linked list"
    ll_obj.appendNode(3)
    ll_obj.printNodes()
    print "Appending 4 to the linked list"
    ll_obj.appendNode(4)
    ll_obj.printNodes()
    print "Appending 5 to the linked list"
    ll_obj.appendNode(5)
    ll_obj.printNodes()
    print "Inserting 2 at position 1  to the linked list"
    ll_obj.insertNode(2,1)
    ll_obj.printNodes()
    print "Deleting node with data 4 in the linked list"
    ll_obj.deleteNode(2)
    ll_obj.printNodes()
    print "Trying to delete an item not in the list - 20"
    ll_obj.deleteNode(20)
    ll_obj.printNodes()
    rev_obj = ll_obj.reverseList()
    print "Printing linked list after reversing"
    ll_obj.printNodes()
    print "Printing original linked list"
    ll_obj.insert_into_sorted(2)
    ll_obj.insert_into_sorted(0)
    ll_obj.insert_into_sorted(21)
    print ll_obj.printNodes()
    rev_obj.printNodes()
    if ll_obj.checkPalindromeLists(rev_obj) :
        print "Linked lists are palindrome"
    else :
        print "Linked lists are not palindrome"
    
