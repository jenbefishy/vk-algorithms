from linked_list import Node, LinkedList
import unittest

'''
Необходимо написать функцию, которая принимает на вход односвязный список и некоторое целое число val. Необходимо удалить узел из списка, значение которого равно val.
'''

def removeElement(head: Node, val: int) -> Node:
    dummy = Node(None)
    dummy.next = head
    prev = dummy
    cur = head

    while cur is not None:
        if cur.data == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next

class TestRemoveElement(unittest.TestCase):
    def test_case_1(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        
        new_head = removeElement(llist.head, 3)
        
        result = []
        while new_head:
            result.append(new_head.data)
            new_head = new_head.next
        self.assertEqual(result, [1, 2, 4])
    
    def test_case_2(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        
        new_head = removeElement(llist.head, 5)
        
        result = []
        while new_head:
            result.append(new_head.data)
            new_head = new_head.next
        self.assertEqual(result, [1, 2, 3])
    
    def test_case_3(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        
        new_head = removeElement(llist.head, 1)
        
        result = []
        while new_head:
            result.append(new_head.data)
            new_head = new_head.next
        self.assertEqual(result, [2])
    
    def test_case_4(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        
        new_head = removeElement(llist.head, 3)
        
        result = []
        while new_head:
            result.append(new_head.data)
            new_head = new_head.next
        self.assertEqual(result, [1, 2])
    
    def test_case_5(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(3)
        
        new_head = removeElement(llist.head, 2)
        
        result = []
        while new_head:
            result.append(new_head.data)
            new_head = new_head.next
        self.assertEqual(result, [1, 3])
    
    def test_case_6(self):
        llist = LinkedList()
        new_head = removeElement(llist.head, 1)
        self.assertIsNone(new_head)

if __name__ == "__main__":
    unittest.main()
