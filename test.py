__author__ = 'Sam'

import binascii
import os

try:
    f = open('D:\Dropbox\RWTH\HiWi\descriptor\descriptor_set_00_80.points', 'rb')
    while True:
        file_data = f.read(1024)
        if not file_data:
            break
        print(binascii.hexlify(file_data))
        print(len("First"))
        print("FileSize: ", os.path.getsize('D:\Dropbox\RWTH\HiWi\descriptor\descriptor_set_00_80.points'))
except IOError as e:
    print(e.errno)
    print(e)
finally:
    f.close()
