class Node:
    """
            The Node class is a blueprint for creating nodes in the linked list.
            Each node has a data attribute to store the value of the node.
            It also has a next attribute, initially set to None, to reference the next node in the list.
    """

    def __init__(self, data):
        self.data = data  # Assign data
        self.nextPointer = None  # Initialize nextPointer as NULL


class LinkedList:
    '''
        The LinkedList class has a single attribute head, which initially points to None indicating an empty list.
    '''

    def __init__(self):
        self.__head = None  # Intialize Head(START) Pointer as Null

    def isEmpty(self):
        '''
            This method checks if the linked list is empty by examining whether the head is None.
        '''
        if self.__head == None:
            return True
        else:
            return False

    def print_list(self):
        """
            Displays the elements of a linked list from the head to the end.
            Parameters:
                - self: The linked list object.
            Returns:
                - None: Prints the elements of the linked list followed by "None" to signify the end.
            Example:
                >>> linked_list = LinkedList()
                >>> linked_list.insert_at_head(3)
                >>> linked_list.insert_at_head(2)
                >>> linked_list.insert_at_head(1)
                >>> linked_list.display_linked_list()
                1 -> 2 -> 3 -> None
        """
        current_node = self.__head  # This is the starting point for traversing the list.
        while current_node:  # Start a loop that continues as long as current_node is not None. This loop will iterate through each node in the linked list.
            print(current_node.data, end=" ---> ")
            # Move to the next node in the linked list by updating current_node to be the next node.
            current_node = current_node.nextPointer
        print("None")  # Print "None" to indicate the end of the linked list

    def insertionAtHeadOfNode(self, data):
        """
            This method inserts a new node at the beginning of the linked list.
            It takes a data parameter, creates a new node with that data using the Node class, and sets the nextPointer of the new node to the current head of the list.
            Then, it updates the head of the list to be the new node.
        """
        new_Node = Node(data)
        #  Make next of new Node as head
        new_Node.nextPointer = self.__head
        #  Move the head to point to new Node
        self.__head = new_Node


    def insertionAtEndofNode(self, data):
        """
            Inserts a new node with the given data at the end of the linked list.

            Parameters:
                - self: The linked list object.
                - data: The data to be inserted in the new node.

            Returns:
                - None: Modifies the linked list in place.

            Example:
                >>> linked_list = LinkedList()
                >>> linked_list.insert_at_end(1)
                >>> linked_list.insert_at_end(2)
                >>> linked_list.insert_at_end(3)
                >>> linked_list.display_linked_list()
                1 -> 2 -> 3 -> None
        """
        new_Node = Node(data) # Create a new node with the given data

        if self.__head == None: # Check if the linked list is empty
            self.__head = new_Node  # If empty, set the new node as the head
            return
        
        last_Node = self.__head # Start from the head of the linked list
        while last_Node.nextPointer:
            last_Node = last_Node.nextPointer # Traverse the linked list to find the last node

        last_Node.nextPointer = new_Node  # Set the next pointer of the last node to the new node


linked_list = LinkedList()

print("Original Linked List:")
linked_list.print_list()

linked_list.insertionAtHeadOfNode(1)
linked_list.print_list()

linked_list.insertionAtHeadOfNode(2)
linked_list.print_list()

linked_list.insertionAtHeadOfNode(3)
linked_list.print_list()

linked_list.insertionAtHeadOfNode(4)
linked_list.print_list()

linked_list.insertionAtHeadOfNode(5)
linked_list.print_list()

linked_list.insertionAtEndofNode(7)
linked_list.print_list()

linked_list.insertionAtEndofNode(8)
linked_list.print_list()

linked_list.insertionAtEndofNode(9)
linked_list.print_list()

linked_list.insertionAtEndofNode(10)
linked_list.print_list()

print("Changed Linked List:")
linked_list.print_list()
