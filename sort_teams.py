import sys
from model import create_linked_list, create_init_pools, print_pools

# First create a linked list of participates
LL = create_linked_list(sys.argv[1])

# use LL to create init_pools
init_pools = create_init_pools(LL)

# print init_pools[0]
# print '------------'
# print init_pools[1]
# print '------------'
# print init_pools[2]
# print '------------'
# print init_pools[3]

print_pools(init_pools)
