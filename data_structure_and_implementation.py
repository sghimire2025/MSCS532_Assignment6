
# Arrays and Matrices 
# -----------------------------
class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value

    def delete(self, index):
        if 0 <= index < self.size:
            self.data[index] = None

    def access(self, index):
        return self.data[index] if 0 <= index < self.size else None
    
print("\tARRAY DEMO ")
arr = Array(5)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
print(arr.access(0))  # Output: 10
print(arr.access(1))  # Output: 20
arr.delete(1)
print(arr.access(1))  # Output: None


# Stack using Array (LIFO)
# -----------------------------
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

print("\n\tSTACK DEMO")
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.peek())    # Output: 10
print(stack.pop())     # Output: 10
print(stack.pop())     # Output: 5
print(stack.pop())     # Output: None

# Queue using Array (FIFO)
# -----------------------------
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0
print("\n\tQUEUE DEMO")
queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
print(queue.dequeue())  # Output: 100
print(queue.dequeue())  # Output: 200
print(queue.dequeue())  # Output: None


# Singly Linked List
# -----------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

print("\n\tLINKED LIST DEMO ")
linked_list = LinkedList()
linked_list.insert_at_head(1)
linked_list.insert_at_head(2)
linked_list.insert_at_head(3)
linked_list.traverse()  # Output: 3 -> 2 -> 1 -> None
linked_list.delete_head()
linked_list.traverse()  # Output: 2 -> 1 -> None

# Rooted Tree (using Linked List structure)
# -----------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of TreeNode instances

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.traverse(level + 1)


print("\n\t ROOTED TREE DEMO")
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
root.add_child(b)
root.add_child(c)
b.add_child(TreeNode("D"))
b.add_child(TreeNode("E"))
c.add_child(TreeNode("F"))
root.traverse()
