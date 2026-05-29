
# python code splitter

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at specific position
    def insert_at_position(self, position, data):
        new_node = Node(data)

        if position == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
            return

        temp.next = temp.next.next

    # Search element
    def search(self, key):
        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                return position

            temp = temp.next
            position += 1

        return -1

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Driver Code
ll = LinkedList()

# Insert operations
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

ll.insert_at_position(2, 15)

print("Linked List:")
ll.display()

# Delete operations
ll.delete_from_beginning()
print("\nAfter deleting from beginning:")
ll.display()

ll.delete_from_end()
print("\nAfter deleting from end:")
ll.display()

ll.delete_by_value(15)
print("\nAfter deleting value 15:")
ll.display()

# Search operation
position = ll.search(20)

if position != -1:
    print(f"\n20 found at position {position}")
else:
    print("\n20 not found")

# Count nodes
print("\nTotal Nodes:", ll.count_nodes())

# Reverse linked list
ll.reverse()
print("\nReversed Linked List:")
ll.display()
"""

# initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

# perform the split
chunks = splitter.split_text(text)

print(f"length of chunk: {len(chunks)}")
print(f"chunk content: {chunks[0]}")