
from code.linked_list import LinkedList

class TestLinkedList:

    def test_linkedlist_constructor(self):
        t = LinkedList(1)
        t.print_list()

    def test_linkedlist_append(self):
        t = LinkedList(1)
        t.append(2)
        t.append(3)
        t.append(4)
        t.append(5)
        t.append(6)
        t.print_list()

    def test_linkedlist_prepend(self):
        t = LinkedList(1)
        t.prepend(0)
        t.print_list()

    def test_linkedlist_pop(self):
        t = LinkedList(1)
        t.pop()
        t.print_list()



