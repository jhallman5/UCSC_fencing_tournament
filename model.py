import csv
from linked_list import Node, Linked_List

def create_linked_list(fencers_csv):
    ''' Creates a sorted linked list from a CSV file. '''
    with open(fencers_csv) as csv_file:
        fencer_list = Linked_List()
        reader = csv.reader(csv_file, delimiter='\t')
        for row in reader:
            fencer = {
            'last_name': row[0].split(',')[0],
            'first_name': row[0].split(',')[1],
            'team': row[0].split(',')[2],
            'rank':row[0].split(',')[3]
            }
            fencer_list.insert(fencer)
        return fencer_list

def create_init_pools(linked_list):
    ''' Returns a list of initial pools of equal difficulty using a serpentine sorting method. '''
    num_pools = determine_num_pools(linked_list)
    sorted_list = []
    init_pools = []
    for i in range(0, num_pools):
        init_pools.append([])
    current_node = linked_list.head
    direction_forward = False
    while current_node:
        sorted_list.append(current_node.data)
        current_node = current_node.next_node
    for index, fencer in enumerate(sorted_list):
        if sorted_list.index(fencer) % num_pools == 0:
            direction_forward = not direction_forward
        if direction_forward:
            init_pools[index % num_pools].append(fencer)
        else:
            init_pools[(num_pools - 1) - (index % num_pools)].append(fencer)
    return init_pools

def determine_num_pools(linked_list):
    ''' Returns the number of pools. '''
    Num_fencers = linked_list.length
    if check_pool_size(Num_fencers, 6):
        return int(Num_fencers / 6)
    if check_pool_size(Num_fencers, 7):
        return int(Num_fencers / 7)
    if check_pool_size(Num_fencers, 5):
        return int(Num_fencers / 5)

def check_pool_size(num_fencers, proposed_pool_size):
    '''
        Determines how many pools there will be of the proposed size.
        Returns boolean: if remaining fencers can fit into number of pools without exceeding + 1.
     '''
    number_of_pools = int(num_fencers / proposed_pool_size)
    remaining_fencers = num_fencers - (number_of_pools * proposed_pool_size)
    if remaining_fencers / number_of_pools <= 1 :
        return True
    return False

def sort_pools(init_pools, linked_list):
    ''' Returns a final sorted list of pools. '''
    TRS = teams_requiring_sorting(linked_list)
    num_pools = determine_num_pools(linked_list)
    final_pools = init_pools
    for team, member_count in TRS.items():
        min_members_per_pool = int(member_count / num_pools)
        remaining_max_pools = member_count % num_pools
        pool_arg = find_pool_arrangment(init_pools, team)
        pool_accept = find_pool_acceptability(pool_arg, min_members_per_pool)
        handled_pools = handle_pool_excess(pool_accept,remaining_max_pools )
        final_pools = swap_members(final_pools, handled_pools, team, TRS)
    return final_pools

def find_pool_arrangment(init_pools, team):
    ''' Returns a list of currnet pool (uneven) distrubution. '''
    pool_arrangement = []
    for index, pool in enumerate(init_pools):
        pool_arrangement.append(0)
        for player in pool:
            if player.get('team').strip() == team:
                pool_arrangement[index] += 1
    return pool_arrangement

def find_pool_acceptability(pool_arrangement, min_members_per_pool):
    ''' Returns a list of pools with the ability to receive additional members. '''
    pool_acceptability = []
    for current_member_count in pool_arrangement:
        pool_acceptability.append(min_members_per_pool - current_member_count)
    return pool_acceptability

def handle_pool_excess(PA,remaining_max_pools):
    ''' Handles the modulo of pool acceptibility. '''
    limit_max_pools = []
    pool_excess = remaining_max_pools
    for pool in PA:
        if pool < 0 and pool_excess > 0:
            limit_max_pools.append(pool + 1)
            pool_excess -= 1
        else:
            limit_max_pools.append(pool)
    return limit_max_pools

def swap_members(current_pools, handled_pools, team, TRS):
    ''' Handles swaps of members. '''
    pool_index_to_move = []
    pool_index_to_accept = []
    for index, pool in enumerate(handled_pools):
        if pool < 0:
            pool_index_to_move.append(index)
        if pool >= 0:
            pool_index_to_accept.append(index)
    if not len(pool_index_to_move):
        return current_pools
    for index, pool in enumerate(pool_index_to_move):
        num_players_to_remove = abs(handled_pools[pool])
        possible_rm_moves = []
        for player in current_pools[pool_index_to_move[index]]:
            if player.get('team').strip() == team:
                if len(possible_rm_moves) < num_players_to_remove:
                    possible_rm_moves.append(player)
                else:
                    for inner_index, possible_player in enumerate(possible_rm_moves):
                        p_rank = possible_player.get('rank')
                        new_p_rank = player.get('rank')
                        if ord(p_rank[0]) < ord(new_p_rank[0]):
                            possible_rm_moves[inner_index] = player
                            break
                        if ord(p_rank[0]) == ord(new_p_rank[0]):
                            if p_rank[1:] > new_p_rank[1:]:
                                possible_rm_moves[inner_index] = player
        for x in range(len(possible_rm_moves)):
            player_to_swap = possible_rm_moves[x]
            p_rank = player_to_swap.get('rank')
            location_to_swap = find_location_to_swap(current_pools, p_rank, TRS, current_pools[pool_index_to_move[index]])
            swap_a_store = current_pools[location_to_swap[0]][location_to_swap[1]]
            player_to_swap_index = current_pools[pool_index_to_move[index]].index(player_to_swap)
            swap_b_store = current_pools[pool_index_to_move[index]][player_to_swap_index]
            current_pools[location_to_swap[0]][location_to_swap[1]] = swap_b_store
            current_pools[pool_index_to_move[index]][player_to_swap_index] = swap_a_store
    return current_pools

def find_location_to_swap(pools, rank, TRS, pool_index_to_move):
    ''' Returns tuple of coordinates to swap. '''
    for idx, pool in enumerate(pools):
        if not idx == pools.index(pool_index_to_move):
            for index, player in enumerate(pool):
                if player.get('team').strip() == '':
                    PR = player.get('rank')
                    if ord(rank[0]) < ord(PR[0]):
                        return (idx, index)
                    if ord(rank[0]) == ord(PR[0]):
                        if rank[1:] > PR[1:]:
                            return (idx, index)
                if player.get('team').strip() not in TRS.keys():
                    PR = player.get('rank')
                    if ord(rank[0]) < ord(PR[0]):
                        return (idx, index)
                    if ord(rank[0]) == ord(PR[0]):
                        if rank[1:] > PR[1:]:
                            return (idx, index)

def teams_requiring_sorting(linked_list):
    ''' Returns a dict of team:member_count which are > 1.'''
    current_node = linked_list.head
    teams_dict = {}
    while current_node:
        team = current_node.data.get('team').strip()
        if not teams_dict.get(team):
            teams_dict[team] = 1
        else:
            teams_dict[team] += 1
        current_node = current_node.next_node
    return {k:v for k,v in teams_dict.items() if v > 1 and len(k)}

def print_pools(pools):
    print 'Pool List'
    for index, pool in enumerate(pools):
        print '-)------ Pool # %s ------(- (%s)' % ((index + 1), len(pool))
        for player in pool:
            print '\t'.join((player.get('first_name'), player.get('last_name'), player.get('team'), player.get('rank')[0], player.get('rank')[1:]))
