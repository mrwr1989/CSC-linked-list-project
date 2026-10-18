
import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def test_append_prepend(self):
        linked = SinglyLinkedList()
        self.assertTrue(linked.is_empty())
        linked.append(20)
        linked.prepend(10)
        linked.append(30)
        self.assertEqual(list(linked), [10, 20, 30])
        self.assertEqual(len(linked), 3)
        self.assertEqual(linked._tail.data, 30)
        self.assertIsNone(linked._tail.next)

    def test_forward_build(self):
        values = [10, 20, 30, 40, 50]
        linked = SinglyLinkedList()
        linked.build_list_forward(values)
        self.assertEqual(list(linked), values)
        self.assertEqual(values, [10, 20, 30, 40, 50])
        self.assertEqual(len(linked), 5)

    def test_backward_build(self):
        values = [10, 20, 30, 40, 50]
        linked = SinglyLinkedList()
        linked.build_list_backward(values)
        self.assertEqual(list(linked), [50, 40, 30, 20, 10])
        self.assertEqual(values, [10, 20, 30, 40, 50])

    def test_queries(self):
        linked = SinglyLinkedList()
        self.assertTrue(linked.is_empty())
        self.assertFalse(linked.contains(10))
        self.assertEqual(len(linked), 0)
        linked.append(10)
        linked.append(20)
        self.assertFalse(linked.is_empty())
        self.assertTrue(linked.contains(20))
        self.assertFalse(linked.contains(99))
        self.assertEqual(list(linked), [10, 20])

    def test_insert_after(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30])
        linked.insert_after(20, 25)
        linked.insert_after(30, 40)
        self.assertEqual(list(linked), [10, 20, 25, 30, 40])
        self.assertEqual(linked._tail.data, 40)
        self.assertIsNone(linked._tail.next)
        with self.assertRaises(ValueError):
            linked.insert_after(99, 100)

    def test_remove_positions(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([10, 20, 30, 40])
        linked.remove(10)
        linked.remove(30)
        linked.remove(40)
        self.assertEqual(list(linked), [20])
        self.assertEqual(linked._head, linked._tail)
        linked.remove(20)
        self.assertTrue(linked.is_empty())
        self.assertIsNone(linked._head)
        self.assertIsNone(linked._tail)
        self.assertEqual(len(linked), 0)

        with self.assertRaises(ValueError):
            linked.remove(99)

    def test_remove_all(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([2, 2, 3, 2, 4, 2, 2])
        self.assertEqual(linked.remove_all(2), 5)
        self.assertEqual(list(linked), [3, 4])
        self.assertEqual(len(linked), 2)
        self.assertEqual(linked._tail.data, 4)
        self.assertIsNone(linked._tail.next)
        self.assertEqual(linked.remove_all(99), 0)

    def test_remove_all_to_empty(self):
        linked = SinglyLinkedList()
        linked.build_list_forward([5, 5, 5])
        self.assertEqual(linked.remove_all(5), 3)
        self.assertTrue(linked.is_empty())
        self.assertIsNone(linked._head)
        self.assertIsNone(linked._tail)
        self.assertEqual(len(linked), 0)


if __name__ == "__main__":
    unittest.main()
