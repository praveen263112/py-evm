from eth.vm.forks.berlin.headers import (
    compute_berlin_difficulty,
)
from eth.vm.forks.berlin.headers import (
    configure_header,
    create_header_from_parent,
)


compute_praveen_difficulty = compute_berlin_difficulty

create_praveen_header_from_parent = create_header_from_parent(
    compute_praveen_difficulty
)
configure_praveen_header = configure_header(compute_praveen_difficulty)
