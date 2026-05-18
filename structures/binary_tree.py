class Node:
    def __init__(self, value=None, left=None, right=None, parent=None, x=None, y=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

        self.x = x
        self.y = y

class BinaryTree():
    def __init__(self, root=None):
        self.root = root
        self.count = 0
        self.max_nodes = 10

    def add_node(self, value):

        if self.root is None:
            self.root = self.create_node(value)

            self.root.x = 0
            self.root.y = 0

            return

        self._insert_recursive(self.root, value, depth=1)

    def _insert_recursive(self, current, value, depth):   
        spacing = 1 / (2 ** (depth - 1))

        if value < current.value:
            if current.left is None:
                node = self.create_node(value)

                node.parent = current
                current.left = node

                node.x = current.x - spacing  # move node to left of parent
                node.y = current.y - 1  # move node below parent                     
            else:
                self._insert_recursive(current.left, value, depth + 1)
        else:
            if current.right is None:
                node = self.create_node(value)

                node.parent = current
                current.right = node

                node.x = current.x + spacing
                node.y = current.y - 1
            else:
                self._insert_recursive(current.right, value, depth + 1)    



    def create_node(self, value):

        if value != None:
            newNode = Node(value)

        if self.count >= self.max_nodes:
            return    
        self.count = self.count + 1   

        return newNode

    def delete(self, value):
        pass

    def get_nodes(self, node, nodes=None):
        if nodes is None:
            nodes = []
        
        if node:
            nodes.append(node)

            self.get_nodes(node.left, nodes)
            self.get_nodes(node.right, nodes)

        return nodes   

    def get_tree(self):
        return self.get_nodes(self.root)             








def main():
    
    binary_tree = BinaryTree()

    binary_tree.add_node(5)
    binary_tree.add_node(3)
    binary_tree.add_node(7)
    binary_tree.add_node(9)
    binary_tree.add_node(1)
    binary_tree.add_node(10)
    binary_tree.add_node(1000)

    my_array = binary_tree.get_tree()

    print(my_array)

if __name__ == "__main__":
    main()




