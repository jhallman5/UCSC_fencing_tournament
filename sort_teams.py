import sys
from model import create_linked_list, create_init_pools, sort_pools, print_pools, check_length

# Create a linked list of players
LL = create_linked_list(sys.argv[1])

# Check number of players
check_length(LL)

# Use LL to create initial pools
init_pools = create_init_pools(LL)

# Sort initial pools
sorted_pools = sort_pools(init_pools, LL)

# print pools
print_pools(sorted_pools)
