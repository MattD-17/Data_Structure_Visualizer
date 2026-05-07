

class Queue:

    def __init__(self):
        self.max_size = 10
        self.items = [None] * self.max_size
        self.count = 0
        self.front = 0
        self.back = 0


    def enqueue(self, item):
        if self.count == self.max_size:
            return
        self.items[self.back] = item
        count = count + 1
        self.back = self.back + 1

        if self.back == self.max_size and self.count < self.max_size:
            self.back = self.back % self.max_size




    def dequeue(self, item):
