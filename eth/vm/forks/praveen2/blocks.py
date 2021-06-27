from rlp.sedes import (
    CountableList,
)
from eth.rlp.headers import (
    BlockHeader,
)
from eth.vm.forks.frontier.blocks import (
    FrontierBlock,
)

from .transactions import (
    Praveen2Transaction,
)


class Praveen2Block(FrontierBlock):
    transaction_builder = Praveen2Transaction
    fields = [
        ('header', BlockHeader),
        ('transactions', CountableList(transaction_builder)),
        ('uncles', CountableList(BlockHeader))
    ]
