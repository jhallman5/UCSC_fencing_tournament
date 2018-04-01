import sys
from model import create_linked_list, create_init_pools, sort_pools, print_pools

# First create a linked list of players
LL = create_linked_list(sys.argv[1])

# Use LL to create initial pools
init_pools = create_init_pools(LL)

# Sort initial pools
sorted_pools = sort_pools(init_pools, LL)

# Finally print pools
# print_pools(init_pools)
