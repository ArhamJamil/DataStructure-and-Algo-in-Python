class Node:
    def __init__(self, item=None, next=None):
        # Node constructor to initialize node attributes
        self.item = item  # Data in the node
        self.next = next  # Reference to the next node


class Singly_Linked_List:
    def __init__(self, start=None):
        # Singly linked list constructor
        self.start = start  # Reference to the first node in the list

    def is_empty(self):
        # Check if the list is empty
        if self.start is None:
            return True
        else:
            return False

    def insert_at_start(self, data):
        # Insert a new node at the beginning of the list
        new_node_reference = Node(data)
        new_node_reference.next = self.start
        self.start = new_node_reference

    def insert_at_last(self, data):
        # Insert a new node at the end of the list
        new_node_reference = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node_reference
        else:
            # If the list is empty, the new node becomes the start
            self.start = new_node_reference

    def search(self, data):
        # Search for a node with a specific data value
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp  # If data is found, return the node
            temp = temp.next
        return None  # If data is not found, return None

    def insert_after(self, data, value):
        # Insert a new node after a node with a specific data value
        temp = self.search(value)
        if temp is not None:
            new_node_reference = Node(data)
            new_node_reference.next = temp.next
            temp.next = new_node_reference

    def print_list(self):
        # Print the elements of the list
        temp = self.start
        while temp is not None:
            print(temp.item, end=" => ", sep=" ")
            temp = temp.next

    def delete_at_first(self):
        # Delete the first node in the list
        if self.start is not None:
            self.start = self.start.next
        else:
            print("List is empty, can't delete")

    def delete_at_last(self):
        # Delete the last node in the list
        if self.start is None:
            print("List is empty, can't delete")
        elif self.start.next is None:
            # If there's only one node, set start to None
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        # Delete a node with a specific data value
        if self.start is None:
            print("List is empty, can't delete")
        elif self.start.next is None:
            # If there's only one node and it matches the data, set start to None
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                # If the first node matches the data, set start to the next node
                self.start = temp.next
            else:
                # Iterate through the list to find and delete the node with the specified data
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                    else:
                        temp = temp.next



obj = Singly_Linked_List()

obj.insert_at_start(10)
obj.insert_at_start(20)
obj.insert_at_start(30)

obj.insert_at_last(40)
obj.insert_at_last(50)
obj.insert_at_last(60)

print(obj.Search(30))
print(obj.Search(70))
print(obj.Search(20))

obj.insert_after(70, 30)
obj.insert_after(80, 60)

obj.print_list()
print("")

obj.delete_at_first()
obj.delete_at_last()
obj.delete_at_last()

obj.print_list()
print("")

obj.delete_item(10)
obj.print_list()
print("")

obj.delete_item(70)
obj.print_list()





