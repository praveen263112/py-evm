from eth.vm.forks.frontier.headers import (
    compute_frontier_difficulty,
)
from eth.vm.forks.frontier.headers import (
    configure_frontier_header,
    create_frontier_header_from_parent,
)


compute_praveen2_difficulty = compute_frontier_difficulty

create_praveen2_header_from_parent = create_frontier_header_from_parent
configure_praveen2_header = configure_frontier_header
