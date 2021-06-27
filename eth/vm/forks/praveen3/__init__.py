from typing import (
    Type,
)


from eth.rlp.blocks import BaseBlock
from eth.vm.forks.frontier import (
    FrontierVM,
)
from eth.vm.state import BaseState

from .blocks import Praveen3Block
from .headers import (
    compute_praveen3_difficulty,
    configure_praveen3_header,
    create_praveen3_header_from_parent,
)
from .state import Praveen3State
from .validation import validate_praveen3_transaction_against_header
from eth.abc import (
    BlockAPI,
    BlockHeaderAPI,
    ReceiptAPI,
    StateAPI,
    SignedTransactionAPI,
    ComputationAPI,
)

class Praveen3VM(FrontierVM):
    # fork name
    fork = 'praveen3'

    # classes
    block_class: Type[BaseBlock] = Praveen3Block
    _state_class: Type[BaseState] = Praveen3State

    # Methods
    create_header_from_parent = staticmethod(create_praveen3_header_from_parent)  # type: ignore
    compute_difficulty = staticmethod(compute_praveen3_difficulty)    # type: ignore
    configure_header = configure_praveen3_header
    validate_transaction_against_header = validate_praveen3_transaction_against_header
