class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        pass

def print_tree(root):
    if root is None:
        return
    print(root.data, end=':')

    if root.left is not None:
        print('l', root.left.data, end=' ')
    if root.right is not None:
        print('r', root.right.data, end=' ')
    print()

    print_tree(root.left)
    print_tree(root.right)

def input_tree():
    root_data = int(input())
    if root_data == 0:
        return None

    root = Node(root_data)

    leftroot = input_tree()
    rightroot = input_tree()
    root.left = leftroot
    root.right = rightroot

    return root

def num_nodes(root):
    if root is None:
        return 0

    left_count = num_nodes(root.left)
    right_count = num_nodes(root.right)

    return left_count + right_count + 1

def sum_nodes(root):
    if root is None:
        return 0

    left_sum = sum_nodes(root.left)
    right_sum = sum_nodes(root.right)

    return left_sum + right_sum + root.data

def print_tree_pre(root):
    if root is None:
        return
    print(root.data)

    print_tree_pre(root.left)
    print_tree_pre(root.right)

def print_tree_post(root):
    if root is None:
        return

    print_tree_post(root.left)
    print_tree_post(root.right)
    print(root.data)

def print_tree_in(root):
    if root is None:
        return

    print_tree_in(root.left)
    print(root.data)
    print_tree_in(root.right)

def largest_node(root):
    if root is None:
        return 0

    left_large = largest_node(root.left)
    right_large = largest_node(root.right)
    largest = max(left_large, right_large, root.data)

    return largest

def greater_than(root, x):
    if root is None:
        return 0

    left_count = greater_than(root.left, x)
    right_count = greater_than(root.right, x)

    if root.data > x:
        return left_count + right_count + 1
    return left_count + right_count

def tree_height(root):
    if root is None:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    height = max(left_height, right_height) + 1
    return height

def

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

node1.left = node2
node2.left = node3
node3.right = node4
node2.right = node5

# root = input_tree()

# print_tree(node1)
# print(num_nodes(node1))
print_tree(node1)
print()
# print_tree_post(node1)
print()
# print_tree_in(node1)
# print(sum_nodes(node1))
print(tree_height(node1))
