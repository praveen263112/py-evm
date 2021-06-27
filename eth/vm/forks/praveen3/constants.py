from eth_typing import (
    Address
)

CREATE_CONTRACT_ADDRESS = Address(b'')
FEE_TOKEN_ADDRESS = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x01'
FEE_TOKEN_STORAGE_BALANCE = b"\0"*31 + b"\1"

#
# Difficulty
#
FRONTIER_DIFFICULTY_ADJUSTMENT_CUTOFF = 13


#
# Stack Limit
#
STACK_DEPTH_LIMIT = 1024


#
# Gas Costs and Refunds
#
REFUND_SELFDESTRUCT = 24000
GAS_CODEDEPOSIT = 200