__author__ = 'Sam'

from bluetooth import *
from struct import *
import glob
import os


# Get list of files, read their data
# and send the name, size and bytes
def send_file(socket):
    # Directory to hold descriptors
    os.chdir('D:\Dropbox\RWTH\HiWi\descriptor')
    # List of ".points" files
    names = glob.glob('*.points')

    for name in names:
        # Send the name of the file
        # packed in Modified UTF-8
        name_byte = bytes(name, 'utf-8')
        name_size = pack(">H", len(name_byte))
        name_data = pack(">%ds" % len(name_byte), name_byte)
        socket.send(name_size)
        socket.send(name_data)
        print("File Name: ", name)
        # Send the file's size
        # packed as 4-byte integer
        size = os.path.getsize(name)
        size_data = pack(">i", size)
        size = str(os.path.getsize(name))
        socket.send(size_data)
        print("File Size: ", size)
        # Read 1024 byte data
        f = open(name, 'rb')
        while True:
            data = f.read(1024)
            if not data:
                break
            # Send data in bytes
            socket.send(data)
            print("Packet Size: ", len(data))
        f.close()
    # Return True to indicate completion
    return True


def main():
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "58369c20-ecf6-11e3-ba36-82687f4fc15c"

    advertise_service(server_sock, "SampleServer",
                      service_id=uuid,
                      service_classes=[uuid, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE]
    )

    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        while True:
            finished = send_file(client_sock)
            if finished is True:
                break
                # s = bytes("Hey", 'utf-8')
                # # data = pack("I%ds" % (len(s),), len(s), s)
                # size = pack(">H", len(s))
                # data = pack(">%ds" % len(s), s)
                # for x in range(0, 4):
                #     client_sock.send(size)
                #     client_sock.send(data)
                # break
                # for x in range(0, 4):
                #     client_sock.send('First')
                #     client_sock.send('Second')
                # break
    except IOError as e:
        print(e.errno)
        print(e)

    print("disconnected")

    client_sock.close()
    server_sock.close()
    print("all done")


if __name__ == '__main__':
    main()
