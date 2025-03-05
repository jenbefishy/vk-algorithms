from linked_list import Node, LinkedList
import unittest

'''
Написать функцию, которая принимает на вход два
отсортированных односвязных списка и объединяет их в
один отсортированный список. При этом затраты по памяти должны быть O(1)
'''

def merge(a: Node, b: Node) -> Node:
    dummy = Node(0)
    prev = dummy
    
    while a and b:
        if a.data < b.data:
            prev.next = a
            a = a.next
        else:
            prev.next = b
            b = b.next
        prev = prev.next
    
    prev.next = a if a else b
    
    return dummy.next

class TestMergeSortedLists(unittest.TestCase):
    def linked_list_to_list(self, head: Node):
        result = []
        while head:
            result.append(head.data)
            head = head.next
        return result

    def test_merge_basic(self):
        l1 = LinkedList()
        l1.append(1)
        l1.append(3)
        l1.append(5)

        l2 = LinkedList()
        l2.append(2)
        l2.append(4)
        l2.append(6)

        head = merge(l1.head, l2.head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 3, 4, 5, 6])
    
    def test_merge_with_empty_list(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l2.append(1)
        l2.append(2)
        l2.append(3)
        
        head = merge(l1.head, l2.head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 3])
        
        head = merge(l2.head, l1.head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2, 3])
    
    def test_merge_with_one_element_each(self):
        l1 = LinkedList()
        l1.append(1)

        l2 = LinkedList()
        l2.append(2)
        
        head = merge(l1.head, l2.head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2])
    
    def test_merge_identical_elements(self):
        l1 = LinkedList()
        l1.append(1)
        l1.append(1)
        l1.append(1)
        
        l2 = LinkedList()
        l2.append(1)
        l2.append(1)
        l2.append(1)
        
        head = merge(l1.head, l2.head)
        self.assertEqual(self.linked_list_to_list(head), [1, 1, 1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()


