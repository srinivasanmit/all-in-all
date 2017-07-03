
class Node() :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList() :
    def __init__(self) :
        self.head = None
        self.length = 0

    def appendNodeAtFirst(self, data) :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def getNumberFromList(self) :
        curr_node = self.head
        number = "" 
        while curr_node :
            number += str(curr_node.data)
            curr_node = curr_node.next
        print number
        return int(number)

    def getLengthOfList(self) :
        length = 0
        curr_node = self.head
        while curr_node :
            length += 1
            curr_node = curr_node.next
        return length

    def getLengthOfNumber(self, number) :
        length = 1
        while number / 10 != 0 :
            length += 1
            number = number / 10

    def addNumberToList(self, number_to_add) :
        orig_number = self.getNumberFromList()
        added_number = orig_number + number_to_add
        print "Number after addition - {0}".format(added_number)
        curr_node = self.head
        while curr_node.next :
            curr_node.data = added_number % 10
            curr_node = curr_node.next
            added_number = added_number / 10
        curr_node.data = added_number % 10
        added_number = added_number / 10
        if added_number != 0 :
            new_node = Node(added_number % 10)
            curr_node.next = new_node

    def reverseList(self) :
        curr_node = tmp_curr_node = self.head
        prev_node = None
        while curr_node :
            tmp_curr_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp_curr_node
        self.head = prev_node

    def printNodes(self) :
        curr_node = self.head 
        while curr_node :
            print curr_node.data
            curr_node = curr_node.next

if __name__ == "__main__" :
    ll_obj = LinkedList()
    number_to_insert = int(raw_input("Enter number to be populated in Linked List"))
    while number_to_insert != 0 :
        ll_obj.appendNodeAtFirst(number_to_insert % 10)
        number_to_insert /= 10
    number_to_add = int(raw_input("Enter number to be added "))
    ll_obj.addNumberToList(number_to_add)
    ll_obj.reverseList()
    print "Linked List after addition "
    ll_obj.printNodes()
