class Node:
    def __init__(self, prev=None, next=None, value=None):
        self.prev = prev
        self.next = next
        self.value = value

class LinkedList:
    def __init__(self, head=None, curr=None, tail=None, value=None):
        self.head = head
        self.tail = tail
        self.value = value
        self.curr = curr

    def create_node(self, new_value):
        new_node = Node() # instance of new node
        new_node.value = new_value
        return new_node

    def add_node(self, new_value):
        new_node = self.create_node(new_value)

        if self.head is None: # first node in the list
            self.head = new_node
            self.head.next = None
            self.tail = new_node
            self.curr = new_node
        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
            self.tail.prev = temp

    def delete_node(self):
        if self.head == None:
            print("List is already empty")
        elif self.head == self.tail and not self.head == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def traverse_list(self):
        number_list = []

        while self.curr != None:
            number_list.append(self.curr.value)
            self.curr = self.curr.next
        self.curr = self.head    
        return number_list


