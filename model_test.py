import unittest
import os
from model import create_init_pools, create_linked_list, determine_num_pools, check_pool_size
from linked_list import Linked_List, Node

class Model_test(unittest.TestCase):
    ''' Model unit tests. '''

    def test_create_linked_list(self):
        ''' Tests create_linked_list(fencers_csv). '''
        LL_of_24 = create_linked_list('csv_files/MEconflicts.csv')
        self.assertTrue(isinstance(LL_of_24, Linked_List), 'Creates a LL instance.')
        self.assertTrue(isinstance(LL_of_24.head, Node), 'Creates a LL containing Nodes.')
        self.assertEqual(LL_of_24.length, 24, 'Creates a LL of proper length.')

        LL_of_13 = create_linked_list('csv_files/MEshort.csv')
        self.assertEqual(LL_of_13.length, 13, 'Creates a LL of proper length.')

    def test_check_pool_size(self):
        ''' Tests check_pool_size(num_fencers, proposed_pool_size). '''
        self.assertTrue(check_pool_size(24, 6), 'Should return True if num_feners divides evenly into proposed_pool_size.')
        self.assertTrue(check_pool_size(25, 6), 'Should return True if num_feners balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertTrue(check_pool_size(29, 6), 'Should return True if num_feners balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertTrue(check_pool_size(16, 7), 'Should return True if num_feners balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertTrue(check_pool_size(16, 5), 'Should return True if num_feners balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertTrue(check_pool_size(14, 7), 'Should return True if num_feners balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertFalse(check_pool_size(12, 7), 'Should return False if num_feners does not balances evenly into proposed_pool_size with no pool size greater + 1 ')
        self.assertFalse(check_pool_size(16, 6), 'Should return False if num_feners does not balances evenly into proposed_pool_size with no pool size greater + 1 ')

    def test_determine_num_pools(self):
        ''' Tests determine_num_pools(linked_list). '''
        LL_of_24 = create_linked_list('csv_files/MEconflicts.csv')
        self.assertEqual(determine_num_pools(LL_of_24), 4, 'Should return the correct number of pools given a LL of 24.')

        LL_of_13 = create_linked_list('csv_files/MEshort.csv')
        self.assertEqual(determine_num_pools(LL_of_13), 2, 'Should return the correct number of pools given a LL of 13.')

        LL_of_48 = create_linked_list('csv_files/MEentries.csv')
        self.assertEqual(determine_num_pools(LL_of_48), 8, 'Should return the correct number of pools given a LL of 48.')

    def test_create_init_pools(self):
        '''Tests create_init_pools(linked_list). '''
        LL_of_24 = create_linked_list('csv_files/MEconflicts.csv')
        init_pools = create_init_pools(LL_of_24)
        self.assertEqual(len(init_pools), 4, 'Creates the right amount of pools.')
        self.assertDictEqual(init_pools[0][0], {'first_name': ' Alexander', 'last_name': 'TUROFF', 'rank': 'A15', 'team': 'FISHKILL / CANDLE '}, 'The first index of pool 1 is correct.')
        self.assertDictEqual(init_pools[1][0], {'first_name': ' Tracy', 'last_name': 'COLWELL', 'rank': 'A15', 'team': 'EBFG '}, 'Correctly adds the next ranked player to the next pool.')
        self.assertDictEqual(init_pools[3][0], {'first_name': ' David', 'last_name': 'HITCHCOCK', 'rank': 'A15', 'team': 'NO FEAR '}, 'The last index of the pre-serpentine turn is correct.')
        self.assertDictEqual(init_pools[3][1], {'first_name': ' Mehmet', 'last_name': 'TEPEDELENLIOGLU', 'rank': 'A15', 'team': 'EBFG '}, 'The first index of the post-serpentine turn is correct.')
        self.assertDictEqual(init_pools[2][1], {'first_name': ' Alexandre', 'last_name': 'RACHTCHININE', 'rank': 'A15', 'team': 'NO FEAR'}, 'The second index of the post-serpentine turn is correct.')
        self.assertDictEqual(init_pools[0][2], {'first_name': ' Joseph', 'last_name': 'DEUCHER', 'rank': 'A14', 'team': ''}, 'The third index of the 2nd post-serpentine turn is correct.')
        self.assertDictEqual(init_pools[1][2], {'first_name': ' Kashi', 'last_name': 'WAY', 'rank': 'A14', 'team': 'EBFG '}, 'The third index of the 2nd post-serpentine turn is correct.')

if __name__ == '__main__':
    unittest.main()
