class Stack:
    def __init__(self):
        self.max_size = 10
        self.items = [None] * self.max_size # create initial array
        self.count = 0 # keep track of each item

    def push(self, item):
        if self.count < self.max_size:
            self.items[self.count] = item
            self.count = self.count + 1
        else:
            print("Stack is full")    

    def pop(self):
        if self.count > 0:
            self.count = self.count - 1
        if not self.items[self.count] == None:
            save_item = self.items[self.count]
            self.items[self.count] = None
            return save_item
        return None        

    def peek(self):
        return self.items[self.count]

    def get_items(self):
        return self.items[:self.count]