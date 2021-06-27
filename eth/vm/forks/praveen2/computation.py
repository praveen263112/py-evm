from eth.vm.forks.frontier.computation import (
    FRONTIER_PRECOMPILES
)
from eth.vm.forks.frontier.computation import (
    FrontierComputation,
)

from .opcodes import PRAVEEN2_OPCODES

PRAVEEN2_PRECOMPILES = FRONTIER_PRECOMPILES


class Praveen2Computation(FrontierComputation):
    """
    A class for all execution computations in the ``Praveen2`` fork.
    Inherits from :class:`~eth.vm.forks.constantinople.frontier.FrontierComputation`
    """
    # Override
    opcodes = PRAVEEN2_OPCODES
    _precompiles = PRAVEEN2_PRECOMPILES
