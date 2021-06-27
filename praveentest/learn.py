from eth_utils import remove_0x_prefix, decode_hex, encode_hex
from eth_typing import Address
from eth_hash.auto import keccak
TEST1 = Address(b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x02')
print (type(TEST1));
TEST2 = Address('0x0000000000000000000000000000000000000002')
addr1 = b"\0"*12 + TEST1
print(TEST2)
print(addr1)
print(type(TEST2))
print(type(addr1))
pos1 = b"\0"*31 + b"\1"
print(pos1)

print('1: {}'.format(keccak(addr1+pos1)))
addr2 = bytes.fromhex(remove_0x_prefix(TEST2).rjust(64, '0'))
pos2 = bytes.fromhex(str(1).rjust(64, '0'))
# addr3 = decode_hex(TEST2[2:].rjust(64, '0'))
# pos3 = decode_hex(str(1).rjust(64, '0'))
# # every result are same!
# print('1: {}'.format(keccak(addr1+pos1)))
print('2: {}'.format(keccak(addr2+pos2)))
# print('3: {}'.format(keccak(addr3+pos3)))