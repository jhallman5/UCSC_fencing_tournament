import unittest
from linked_list import Linked_List, Node

class LL_test(unittest.TestCase):
    LL = None

    def setUp(self):
        self.LL = Linked_List()

    def test_init(self):
        self.assertEqual(self.LL.head, None, 'Initial HEAD should be None.')

    def test_insert(self):
        node_1 = {'first_name': ' Keith', 'last_name': 'LICHTEN', 'rank': 'A14', 'team': 'EBFG '}
        self.LL.insert(node_1)
        self.assertDictEqual(node_1, self.LL.head.data, 'Inserting 1 into empty list should create the head.')

        node_2 = {'first_name': ' Alexandre', 'last_name': 'RACHTCHININE', 'rank': 'A15', 'team': 'NO FEAR'}
        self.LL.insert(node_2)
        self.assertDictEqual(node_2, self.LL.head.data, 'Inserting a higher rank node should update the head to point to the new node.')
        self.assertDictEqual(node_1, self.LL.head.next_node.data, 'The previous head should be the new second node. ')

        node_3 = {'first_name': ' Joseph', 'last_name': 'HARRINGTON', 'rank': 'B15', 'team': 'NO FEAR'}
        self.LL.insert(node_3)
        self.assertDictEqual(node_3, self.LL.head.next_node.next_node.data, 'Inserting a low(est) ranking node should insert at the end of the list.')

        node_4 = {'first_name': ' Tomas', 'last_name': 'STRAKA', 'rank': 'A12', 'team': ''}
        self.LL.insert(node_4)
        self.assertDictEqual(node_4, self.LL.head.next_node.next_node.data, 'Inserting an intermediate rank node should insert at the correct location.' )

        node_5 = {'first_name': ' Mehmet', 'last_name': 'TEPEDELENLIOGLU', 'rank': 'A15', 'team': 'EBFG '}
        self.LL.insert(node_5)
        self.assertDictEqual(node_5, self.LL.head.data, 'Inserting an evenly ranked node should insert at the first apprpriate location.')

    def test_is_new_node_higher_rank(self):
        #def is_new_node_higher_rank(self, current, new_node):
        node_1 = Node({'first_name': ' Keith', 'last_name': 'LICHTEN', 'rank': 'A14', 'team': 'EBFG '})
        node_2 = Node({'first_name': ' Alexandre', 'last_name': 'RACHTCHININE', 'rank': 'A15', 'team': 'NO FEAR'})
        node_3 = Node({'first_name': ' Mehmet', 'last_name': 'TEPEDELENLIOGLU', 'rank': 'A15', 'team': 'EBFG '})

        self.assertFalse(self.LL.is_new_node_higher_rank(node_2, node_1), 'Should return false when evaluating a new node that is lower rank than current.')
        self.assertTrue(self.LL.is_new_node_higher_rank(node_1, node_2), 'Should return true when evaluating a new node that is higher rank than current.')
        self.assertTrue(self.LL.is_new_node_higher_rank(node_2, node_3), 'Should return true when evaluating a new node that is equal rank to current.')

if __name__ == '__main__':
    unittest.main()
