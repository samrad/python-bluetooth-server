__author__ = 'Sam'

from struct import *
import base64
import sys
import binascii


s = bytes("Hey", 'utf-8')
size = pack(">H", len(s))
# data = pack(">%ds" % len(s), s)
# pack(">%ds" % len(s), s)
data = pack("I%ds" % (len(s),), len(s), s)
print(size)

# SOLVE THIS FUCKING THING
s1 = 2560
data1 = pack(">i", int(s1))
print(binascii.hexlify(data1))


# test = bytearray(50)
# print("test: ", len(test))
# size_test = "具有"
# print("Chinese: ", sys.getsizeof(size_test))
# b = bytes(size_test.zfill(100 - len(size_test)), 'utf-8')
# print("Chinese: ", sys.getsizeof(b))
# key = bytearray(b"2054")
# name = "1024"
# test = bytearray(name.encode('utf-8')) + bytearray(50 - len(key))
# print("test: ", len(test))
# print(test)

# key1 = bytearray(b"SizeEnd")
# key = base64.b16decode(b'130000000800')
# print(sys.getsizeof(key))
# print("key: ", binascii.hexlify(key))
# print("key1 ", binascii.hexlify(key1))

# print("Before Extend: ", binascii.hexlify(key))
# key.extend(key1)
# print("After Extend: ", binascii.hexlify(key))
# print("test: ", sys.getsizeof(test))

# print(key)