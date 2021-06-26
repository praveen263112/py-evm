from eth.vm.forks.berlin.computation import (
    BERLIN_PRECOMPILES
)
from eth.vm.forks.berlin.computation import (
    BerlinComputation,
)

from .opcodes import PRAVEEN_OPCODES

PRAVEEN_PRECOMPILES = BERLIN_PRECOMPILES


class PraveenComputation(BerlinComputation):
    """
    A class for all execution computations in the ``MuirGlacier`` fork.
    Inherits from :class:`~eth.vm.forks.constantinople.istanbul.IstanbulComputation`
    """
    # Override
    opcodes = PRAVEEN_OPCODES
    _precompiles = PRAVEEN_PRECOMPILES
