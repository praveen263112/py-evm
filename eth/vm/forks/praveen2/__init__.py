from typing import (
    Type,
)


from eth.rlp.blocks import BaseBlock
from eth.vm.forks.frontier import (
    FrontierVM,
)
from eth.vm.state import BaseState

from .blocks import Praveen2Block
from .headers import (
    compute_praveen2_difficulty,
    configure_praveen2_header,
    create_praveen2_header_from_parent,
)
from .state import Praveen2State

from eth.abc import (
    BlockAPI,
    BlockHeaderAPI,
    ReceiptAPI,
    StateAPI,
    SignedTransactionAPI,
    ComputationAPI,
)

class Praveen2VM(FrontierVM):
    # fork name
    fork = 'praveen2'

    # classes
    block_class: Type[BaseBlock] = Praveen2Block
    _state_class: Type[BaseState] = Praveen2State

    # Methods
    create_header_from_parent = staticmethod(create_praveen2_header_from_parent)  # type: ignore
    compute_difficulty = staticmethod(compute_praveen2_difficulty)    # type: ignore
    configure_header = configure_praveen2_header
