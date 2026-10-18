
import unittest
from split_evens_odds import SplitEvensOdds


class TestSplitEvensOdds(unittest.TestCase):

    def make_list(self, values):
        linked = SplitEvensOdds()
        linked.build_list_forward(values)
        return linked

    def check_structure(self, linked, expected):
        self.assertEqual(list(linked), expected)
        self.assertEqual(len(linked), len(expected))

        if expected:
            self.assertEqual(linked._head.data, expected[0])
            self.assertEqual(linked._tail.data, expected[-1])
            self.assertIsNone(linked._tail.next)
        else:
            self.assertIsNone(linked._head)
            self.assertIsNone(linked._tail)

    def test_mixed_numbers(self):
        linked = self.make_list([1, 2, 3, 4, 5, 6, 7, 8])
        even, odd = linked.split_even_odd()

        self.check_structure(even, [2, 4, 6, 8])
        self.check_structure(odd, [1, 3, 5, 7])
        self.check_structure(linked, [])

    def test_all_even(self):
        linked = self.make_list([2, 4, 6, 8])
        even, odd = linked.split_even_odd()

        self.check_structure(even, [2, 4, 6, 8])
        self.check_structure(odd, [])
        self.check_structure(linked, [])

    def test_all_odd(self):
        linked = self.make_list([1, 3, 5, 7])
        even, odd = linked.split_even_odd()

        self.check_structure(even, [])
        self.check_structure(odd, [1, 3, 5, 7])
        self.check_structure(linked, [])

    def test_single_even(self):
        linked = self.make_list([10])
        even, odd = linked.split_even_odd()

        self.check_structure(even, [10])
        self.check_structure(odd, [])
        self.check_structure(linked, [])

    def test_single_odd(self):
        linked = self.make_list([9])
        even, odd = linked.split_even_odd()

        self.check_structure(even, [])
        self.check_structure(odd, [9])
        self.check_structure(linked, [])

    def test_empty_list_error(self):
        linked = SplitEvensOdds()

        with self.assertRaises(ValueError):
            linked.split_even_odd()

    def test_original_nodes_preserved(self):
        linked = self.make_list([1, 2, 3, 4, 5, 6])

        original_nodes = []
        current = linked._head

        while current is not None:
            original_nodes.append(current)
            current = current.next

        even, odd = linked.split_even_odd()

        result_nodes = []

        for result in (even, odd):
            current = result._head

            while current is not None:
                result_nodes.append(current)
                current = current.next

        self.assertEqual(
            {id(node) for node in original_nodes},
            {id(node) for node in result_nodes}
        )

        self.assertEqual(len(result_nodes), len(original_nodes))
        self.check_structure(linked, [])

    def test_inherited_operations(self):
        linked = SplitEvensOdds()
        linked.append(10)
        linked.prepend(5)
        linked.insert_after(10, 20)

        self.assertEqual(list(linked), [5, 10, 20])
        self.assertTrue(linked.contains(10))
        self.assertEqual(len(linked), 3)

        linked.remove(10)
        self.assertEqual(list(linked), [5, 20])


if __name__ == "__main__":
    unittest.main()
