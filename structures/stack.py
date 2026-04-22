class Stack:
    def __init__(self):
        self.items = [] # create initial array
        self.count = 0 # keep track of each item
        self.max_size = 10

    def push(self, item):
        if count < max_size:
            self.items[count] = item
            self.count = self.count + 1
        else:
            print("Stack is full")    

    def pop(self, item):
        if self.items[count]:
            save_item = self.items[count]
            del self.items[count]
            self.count = self.count - 1
            return save_item
        return None        

    def peek(self):
        return self.items[count]

    def get_items(self):
        return self.items