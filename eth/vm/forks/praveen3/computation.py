from eth.vm.forks.frontier.computation import (
    FRONTIER_PRECOMPILES
)
from eth.vm.forks.frontier.computation import (
    FrontierComputation,
)

from .opcodes import PRAVEEN3_OPCODES

PRAVEEN3_PRECOMPILES = FRONTIER_PRECOMPILES


class Praveen3Computation(FrontierComputation):
    """
    A class for all execution computations in the ``Praveen2`` fork.
    Inherits from :class:`~eth.vm.forks.constantinople.frontier.FrontierComputation`
    """
    # Override
    opcodes = PRAVEEN3_OPCODES
    _precompiles = PRAVEEN3_PRECOMPILES
