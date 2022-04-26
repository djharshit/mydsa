class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.bt = None

    def insert_node(self, val):
        if self.bt is None:
            node = Node(val)
            self.bt = node

        if val < self.bt.data:
            if self.bt.left is None:
                node = Node(val)
                self.bt.left = node
            else:
                self.bt.left.insert_node(val)

        elif val > self.bt.data:
            if self.bt.right is None:
                node = Node(val)
                self.bt.right = node
            else:
                self.bt.right.insert_node(val)

        else:
            print('Duplicate nodes')
            return

    def count_node(self):
        count = 0
        if self.bt is not None:
            if self.bt.left is not None:
                count += 1
                self.count_node()

            if self.bt.right is not None:
                count += 1
                self.count_node()

tree = Tree()
tree.insert_node(10)
tree.insert_node(20)
tree.insert_node(15)
tree.insert_node(5)

print(tree.node_count)
