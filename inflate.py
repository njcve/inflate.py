import struct
import sys

binary = sys.argv[1]
null = struct.pack('B', 0)
f = open(binary, 'ab')
f.write(null * 1024 * 1024 * 150)
f.close()
