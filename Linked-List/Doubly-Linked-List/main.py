class Node:
    def __init__(self, prev=None, item=None, next=None):
        # Node constructor to initialize node attributes
        self.prev = prev  # Reference to the previous node
        self.item = item  # Data in the node
        self.next = next  # Reference to the next node


class Doubly_Linked_List:
    def __init__(self, start=None):
        # Doubly linked list constructor
        self.start = start  # Reference to the first node in the list



    def is_empty(self):
        # Check if the list is empty
        if self.start is None:
            return True
        else:
            return False


    def insert_at_start(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(item=data)
        if self.is_empty():
            # If the list is empty, the new node becomes the start
            self.start = new_node
        else:
            # If the list is not empty, adjust references for the new node
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node



    def insert_at_last(self, data):
        # Insert a new node at the end of the list
        temp = self.start
        if self.start is not None:
            # If the list is not empty, find the last node
            new_node = Node(item=data)
            while temp.next is not None:
                temp = temp.next

            # Adjust references for the new node
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            # If the list is empty, the new node becomes the start
            new_node = Node(item=data)
            self.start = new_node



    def Search(self, data):
        # Search for a node with a specific data value
        temp = self.start
        if temp is not None:
            # If the list is not empty, iterate through the list
            while temp.item != data:
                temp = temp.next

            if temp.item == data:
                # If data is found, return the node
                return temp
            else:
                # If data is not found, return None
                return None
        else:
            # If the list is empty, return None
            return None


    def insert_after(self, temp, data):
        # Insert a new node after a given node
        new_node = Node(item=data)
        if temp is not None:
            if temp.next is None:
                # Case: Insert after the last node
                new_node.prev = temp
                temp.next = new_node
            else:
                # Case: Insert between two nodes
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
        else:
            # Case: Insert at the beginning (if temp is None)
            self.start = new_node


    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=" => " )
            temp = temp.next


    def delete_at_start(self):
        temp = self.start
        if temp != None:
            # case: if single node at beginning
            if temp.next == None and temp.prev == None:
                self.start = None
            else:
                self.start = temp.next
                temp.prev = None
        else:
            print("List is Empty Can't delete") 


    def delete_at_last(self):
        temp = self.start
        if temp is not None:
            if temp.next is None:
                # Case: if single node in the list
                self.start = None
            else:
                # Traverse to the last node
                while temp.next is not None:
                    temp = temp.next

                # Update references for the second-to-last node
                temp.prev.next = None
                temp.prev = None
        else:
            print("List is Empty. Can't delete")

    def delete_data(self, data):
        temp = self.start
        while temp is not None and temp.item != data:
            temp = temp.next

        if temp is not None:
                # Case: Node to be deleted is the only node in the list
            if temp.prev is None and temp.next is None:
                self.start = None
            elif temp.next is not None and temp.prev == None:
                # Case: Node to be deleted is the first node
                temp.next.prev = None
                self.start = temp.next
            elif temp.next is None:
                # Case: Node to be deleted is the last node
                temp.prev.next = None
            else:
                # Case: Node to be deleted is in the middle of the list
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = None
    
        else:
            print(f"Node with data {data} not found. Can't delete.")













myList = Doubly_Linked_List()

# INSERTION
myList.insert_at_start(6)
myList.insert_at_last(8)
myList.insert_at_start(10)
myList.insert_after(myList.Search(6), 20)
myList.insert_at_last(30)
myList.insert_at_start(1)
myList.insert_after(myList.Search(20), 40)


myList.print_list()
print(" ")
# DELETIION

myList.delete_data(40)
myList.delete_data(10)
myList.delete_data(1)
# myList.delete_at_last()
# myList.delete_at_start()
myList.delete_data(20)
myList.delete_data(30)
myList.delete_data(8)

myList.print_list()