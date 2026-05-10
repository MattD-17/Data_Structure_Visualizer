

class Queue:

    def __init__(self):
        self.max_size = 10
        self.items = [None] * self.max_size
        self.count = 0
        self.front = 0
        self.back = 0


    def enqueue(self, item):
        
        # Check for full queue
        if self.count == self.max_size:
            return

        # place item at back    
        self.items[self.back] = item
        self.count = self.count + 1
        self.back = self.back + 1



        # if we get to end of queue and queue not full, wrap around
        if self.back == self.max_size and self.count < self.max_size:
            self.back = self.back % self.max_size




    def dequeue(self):

        # Check for empty queue
        if self.count == 0:
            return

        # take item from front and move front forward
        self.items[self.front] = None
        self.front = self.front + 1
        self.count = self.count - 1

        # if dequeing at end of list, wrap around
        if self.front == self.max_size and self.count < self.max_size:
            self.front = 0

    def get_items(self):
        return self.items