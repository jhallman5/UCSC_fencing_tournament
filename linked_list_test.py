import unittest
from linked_list import Linked_List, Node

class LL_test(unittest.TestCase):
    LL = None

    def setUp(self):
        ''' Inits LL. '''
        self.LL = Linked_List()

    def test_init(self):
        ''' Tests Initialization. '''
        self.assertEqual(self.LL.head, None, 'Initial HEAD should be None.')

    def test_insert(self):
        ''' Tests linked_list method: insert. '''
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
        ''' Tests linked_list method: is_new_node_higher_rank(self, current, new_node). '''
        node_1 = Node({'first_name': ' Keith', 'last_name': 'LICHTEN', 'rank': 'A14', 'team': 'EBFG '})
        node_2 = Node({'first_name': ' Alexandre', 'last_name': 'RACHTCHININE', 'rank': 'A15', 'team': 'NO FEAR'})
        node_3 = Node({'first_name': ' Mehmet', 'last_name': 'TEPEDELENLIOGLU', 'rank': 'A15', 'team': 'EBFG '})

        self.assertFalse(self.LL.is_new_node_higher_rank(node_2, node_1), 'Should return false when evaluating a new node that is lower rank than current.')
        self.assertTrue(self.LL.is_new_node_higher_rank(node_1, node_2), 'Should return true when evaluating a new node that is higher rank than current.')
        self.assertTrue(self.LL.is_new_node_higher_rank(node_2, node_3), 'Should return true when evaluating a new node that is equal rank to current.')

    def test_get_letter_rank(self):
        ''' Tests linked_list method: get_letter_rank(self, node). '''
        node_1 = Node({'first_name': ' Keith', 'last_name': 'LICHTEN', 'rank': 'A14', 'team': 'EBFG '})
        self.assertEqual(self.LL.get_letter_rank(node_1), 5, 'A Node of rank A should return 5.')

        node_2 = Node({'first_name': ' Alexandre', 'last_name': 'RACHTCHININE', 'rank': 'B15', 'team': 'NO FEAR'})
        self.assertEqual(self.LL.get_letter_rank(node_2), 4, 'A Node of rank B should return 4.')

        node_3 = Node({'first_name': ' Mehmet', 'last_name': 'TEPEDELENLIOGLU', 'rank': 'C15', 'team': 'EBFG '})
        self.assertEqual(self.LL.get_letter_rank(node_3), 3, 'A Node of rank C should return 3.')

        node_4 = Node({'first_name': ' Alfred', 'last_name': 'ROEBUCK', 'rank': 'D13', 'team': 'NO FEAR'})
        self.assertEqual(self.LL.get_letter_rank(node_4), 2, 'A Node of rank D should return 2.')

        node_5 = Node({'first_name': ' Tracy', 'last_name': 'COLWELL', 'rank': 'E15', 'team': 'EBFG '})
        self.assertEqual(self.LL.get_letter_rank(node_5), 1, 'A Node of rank E should return 1.')

        node_6 = Node({'first_name': ' Tomas', 'last_name': 'STRAKA', 'rank': 'U', 'team': ''})
        self.assertEqual(self.LL.get_letter_rank(node_6), 0, 'A Node of rank U should return 0.')

    # def test_get_year_rank(self):
    #     ''' Tests linked_list method: get_year_rank(self, node). '''
    #

if __name__ == '__main__':
    unittest.main()
