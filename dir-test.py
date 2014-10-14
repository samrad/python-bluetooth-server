__author__ = 'Sam'

import glob
import os

# os.chdir('D:\Dropbox\RWTH\HiWi\descriptor')
# files = glob.glob('*.points')
# for file in files:
#     print(file)
#     try:
#         f = open(file, 'rb')
#         while True:
#             file_data = f.read(1024)
#             if not file_data:
#                 break
#             print(file_data)
#     except IOError as e:
#         print(e.errno)
#         print(e)
#     finally:
#         f.close()


def send_file(socket):
    # Directory to hold descriptors
    os.chdir('D:\Dropbox\RWTH\HiWi\descriptor')
    # List of ".points" files
    names = glob.glob('*.points')

    for name in names:
        f = open(name, 'rb')
        # Send the name of the file
        socket.send(name)
        # Send the file's size
        socket.send(os.path.getsize(name))
        # Read 1024 byte data
        while True:
            data = f.read(1024)
            if not data:
                break
            # Send data in bytes
            socket.send(data)
            print("Sent")


def send_file1():
    # Directory to hold descriptors
    os.chdir('D:\Dropbox\RWTH\HiWi\descriptor')
    # List of ".points" files
    names = glob.glob('descriptor_set_00_80.points')

    for name in names:
        f = open(name, 'rb')
        # Send the name of the file
        print(name)
        # Send the file's size
        print(os.path.getsize(name))
        # Read 1024 byte data
        while True:
            data = f.read(1024)
            if not data:
                break
            # Send data in bytes
            print(data)
            print("Sent")

send_file1()