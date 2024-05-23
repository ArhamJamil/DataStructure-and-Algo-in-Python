class Node:
    def __init__(self, item=None, next=None):
        # Node constructor to initialize node attributes
        self.item = item  # Data in the node
        self.next = next  # Reference to the next node


class Circular_Linked_List:
    def __init__(self, last=None):
        # Circular linked list constructor
        self.last = last  # Reference to the last node in the list

    def is_empty(self):
        # Check if the list is empty
        if self.last == None:
            return True
        else:
            return False
        
    def insert_at_start(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(item=data)
        if self.is_empty():
            # Case: If the list is empty, the new node becomes the start and last
            new_node.next = new_node
            self.last = new_node
        else:
            # Case: If the list is not empty, adjust references for the new node
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_at_last(self, data):
        # Insert a new node at the end of the list
        new_node = Node(item=data)
        if self.is_empty():
            # Case: If the list is empty, the new node becomes the start and last
            new_node.next = new_node
            self.last = new_node
        else:
            # Case: If the list is not empty, adjust references for the new node
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node  # Update the last pointer to the new node



    def Search(self, data):
        # Initialize the temporary node to the first node in the list
        temp = self.last.next
        # Check if the list is empty
        if self.is_empty():
            return None
        else:
            # Iterate through the list until the last node is reached
            while temp != self.last:
                # Check if the current node's item matches the target data
                if temp.item == data:
                    return temp  # Return the node if data is found
                temp = temp.next  # Move to the next node
            # Check the last node separately (to avoid skipping it in the loop)
            if temp == self.last:
                if temp.item == data:
                    return temp  # Return the last node if data is found
            else:
                return None  # Data not found in the list
                
            return None  # Data not found in the list (for completeness)


    def insert_after(self, temp, data):
        # Check if the specified node is None
        if temp is None:
            print("No node found for data to be inserted.")
            return
        else:
            new_node = Node(item=data)
            # Case: Insert after the last node
            if temp == self.last:
                new_node.next = self.last.next
                self.last.next = new_node
                self.last = new_node
            # Case: Insert after a node in a list with only one node
            elif self.last.next == self.last:
                new_node.next = self.last.next
                self.last.next = new_node
                self.last = new_node
            # Case: Insert after a node in a list with multiple nodes
            else:
                new_node.next = temp.next
                temp.next = new_node


    def print_list(self):
        if self.is_empty():
            print("List is empty, No Data present")
        else:
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)


    def delete_first(self):
        if self.is_empty():
            print("List is empty can't delete")
            return
        else:
            # Case: Only One node in the list
            if self.last == self.last.next:
                self.last = None
            else:
                # Case: More than one nodes
                self.last.next = self.last.next.next


    def delete_last(self):
    # Check if the list is empty
        if self.is_empty():
            print("List is empty, can't delete.")
            return
        else:
            # Case: Only One node in the list
            if self.last == self.last.next:
                # If there's only one node, set last to None
                self.last = None
            else:
                # Case: More than one node
                temp = self.last.next
                # Traverse the list until the second-to-last node
                while temp.next != self.last:
                    temp = temp.next
                # Adjust pointers to remove the last node
                temp.next = self.last.next
                self.last = temp


    def delete_item(self, data):
        if self.is_empty():
            print("can't delete list is empty data not found")
            return
        else:
            # Case Only One Node 
            if self.last == self.last.next:
                if self.last.item == data:
                    self.last = None
                print("can't delete as provided data do not match with data in list")
                return
            else:
                temp = self.last.next

                while temp.next != self.last:
                    # Case: Node is the last node 
                    if data == self.last.item:
                        if temp.next == self.last:
                            temp.next = self.last.next
                            self.last = temp
                    # Case: Node is the first Node
                    if data == self.last.next.item:
                        self.last.next = temp.next
                        temp = temp.next

                    # Case Node is in the middle of list
                    if data == temp.next.item:
                        temp.next = temp.next.next

                    temp = temp.next 

                print("can't delete as provided data do not match with data in list")


        


mylist = Circular_Linked_List()

#INSERTION:
mylist.insert_at_start(10)
mylist.print_list()
mylist.insert_at_start(20)
mylist.print_list()
mylist.insert_at_start(30)
mylist.print_list()

mylist.insert_at_last(100)
mylist.print_list()
mylist.insert_at_last(200)
mylist.print_list()
mylist.insert_at_last(300)
mylist.print_list()

mylist.insert_after(mylist.Search(10), 1100)
mylist.print_list()
mylist.insert_after(mylist.Search(1100), 1200)
mylist.print_list()
mylist.insert_after(mylist.Search(1200), 1300)
mylist.print_list()

mylist.insert_after(mylist.Search(300), 1400)
mylist.print_list()
mylist.insert_at_last(400)
mylist.print_list()

#DELETION 
print(" ")

mylist.delete_first()
mylist.print_list()

mylist.delete_last()
mylist.print_list()

mylist.delete_item(300)
mylist.print_list()

mylist.delete_item(20)
mylist.print_list()

mylist.delete_item(1400)
mylist.print_list()
