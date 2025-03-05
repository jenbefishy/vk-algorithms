import unittest
from linked_list import Node, LinkedList

'''
Необходимо написать функцию, которая принимает на вход односвязный список и разворачивает его.
'''

def reverseList(head:Node) -> Node:
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev
    return head

class TestReverseList(unittest.TestCase):
    def test_case_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)

        reversed_head = reverseList(llist.head)

        self.assertEqual(reversed_head.data, 3)
        self.assertEqual(reversed_head.next.data, 2)
        self.assertEqual(reversed_head.next.next.data, 1)
        self.assertIsNone(reversed_head.next.next.next)

    def test_case_2(self):
        llist = LinkedList()
        reversed_head = reverseList(llist.head)
        self.assertIsNone(reversed_head)

    def test_case_3(self):
        llist = LinkedList()
        llist.append(1)
        reversed_head = reverseList(llist.head)
        self.assertEqual(reversed_head.data, 1)
        self.assertIsNone(reversed_head.next)

if __name__ == '__main__':
    unittest.main()
