from eth.vm.forks.berlin.state import (
    BerlinState
)

from .computation import PraveenComputation


class PraveenState(BerlinState):
    computation_class = PraveenComputation
