class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        First Scenario: No item in the list
        Second scenario: When list has nodes
        third Scenario: when list has only 1 node
        """
        temp = self.head
        pre = self.head
        if self.length == 0:
            return None
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        First Scenario: No item in the list
        Second scenario: When list has nodes
        third Scenario: when list has only 1 node
        """
        temp = self.head
        new_node = Node(value)
        if self.length == 0:
            self.append(value)
        else:    
            self.head = new_node
            self.head.next = temp 
        return temp

# my_lk_list = LinkedList(1)
# # my_lk_list.append(2)
# my_lk_list.pop()
# # my_lk_list.append(3)
# # my_lk_list.append(4)
# my_lk_list.print_list()
# print('**----')
# my_lk_list.prepend(5)
# my_lk_list.print_list()

# my_lk_list.pop()
# print('---')
# my_lk_list.print_list()
# my_lk_list.pop()
# print('---')
# my_lk_list.print_list()
# my_lk_list.pop()
# print('---')
# my_lk_list.print_list()
# my_lk_list.pop()
# print('---')
# my_lk_list.print_list()
# #print(my_lk_list.head.value)