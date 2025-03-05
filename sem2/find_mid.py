from linked_list import Node, LinkedList
import unittest

'''
Дан связный список. Необходимо найти середину списка. Сделать это необходимо за O(n) без дополнительных аллокаций
'''

def middleNode(head:Node) -> Node:
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


class TestLinkedListMiddle(unittest.TestCase):
    def test_case_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        self.assertEqual(middleNode(llist.head).data, 3)
    
    def test_case_2(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(middleNode(llist.head).data, 3)
    
    def test_case_3(self):
        llist = LinkedList()
        llist.append(1)
        self.assertEqual(middleNode(llist.head).data, 1)
    
    def test_case_4(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        self.assertEqual(middleNode(llist.head).data, 2)
    
    def test_case_5(self):
        llist = LinkedList()
        self.assertIsNone(middleNode(llist.head))

if __name__ == "__main__":
    unittest.main()
