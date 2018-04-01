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
    teams_requiring_sorting(linked_list)
    # print init_pools
    print '---> ', init_pools[3][2].get('team').strip()
    return init_pools

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
    print 'TRS--> ', {k:v for k,v in teams_dict.items() if v > 1 and len(k)}
    return {k:v for k,v in teams_dict.items() if v > 1 and len(k)}

def print_pools(pools):
    print 'Pool List'
    for index, pool in enumerate(pools):
        print '-)------ Pool # %s ------(- (%s)' % ((index + 1), len(pool))
        for player in pool:
            print '\t'.join((player.get('first_name'), player.get('last_name'), player.get('team'), player.get('rank')[0], player.get('rank')[1:]))
