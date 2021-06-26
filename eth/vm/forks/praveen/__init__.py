from typing import (
    Type,
)

from eth.rlp.blocks import BaseBlock
from eth.vm.forks.berlin import (
    BerlinVM,
)
from eth.vm.state import BaseState

from .blocks import PraveenBlock
from .headers import (
    compute_praveen_difficulty,
    configure_praveen_header,
    create_praveen_header_from_parent,
)
from .state import PraveenState


class PraveenVM(BerlinVM):
    # fork name
    fork = 'praveen'

    # classes
    block_class: Type[BaseBlock] = PraveenBlock
    _state_class: Type[BaseState] = PraveenState

    # Methods
    create_header_from_parent = staticmethod(create_praveen_header_from_parent)  # type: ignore
    compute_difficulty = staticmethod(compute_praveen_difficulty)    # type: ignore
    configure_header = configure_praveen_header
