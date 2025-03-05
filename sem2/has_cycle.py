from linked_list import Node, LinkedList
import unittest

'''
Дан односвязный список. Необходимо проверить, является ли этот список циклическим.

Циклическим (кольцевым) списком называется список у которого последний узел ссылается на один из предыдущих узлов.
'''

def hasCycle(head:Node) -> bool:
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True


class TestLinkedListCycle(unittest.TestCase):
    def test_case_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertFalse(hasCycle(llist.head))

    def test_case_2(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        
        # Create cycle
        llist.head.next.next.next.next = llist.head.next
        self.assertTrue(hasCycle(llist.head))

    def test_case_3(self):
        llist = LinkedList()
        self.assertFalse(hasCycle(llist.head))

    def test_case_4(self):
        llist = LinkedList()
        llist.append(1)
        self.assertFalse(hasCycle(llist.head))

    def test_case_5(self):
        llist = LinkedList()
        llist.append(1)
        llist.head.next = llist.head
        self.assertTrue(hasCycle(llist.head))

if __name__ == "__main__":
    unittest.main()
