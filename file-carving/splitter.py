import os
import sys

# number of repeated null bytes to split the file on
BYTE_LEN = 16

# prefix for split file name, prefix_1, prefix_2, ...
BASE_NAME = 'split'

counter = 0


class FileWriter():
    def __init__(self, filename):
        self.name = filename
        self.fh = open(filename, 'wb')
        self.size = 0

    def write(self, data):
        self.fh.write(data)
        self.size += len(data)

    def close(self):
        self.fh.flush()
        self.fh.close()

        if self.size == 0:
            os.remove(self.name)

with open(sys.argv[1], 'rb') as reader:
    writer = FileWriter("split_%d" % counter)

    while True:
        data = reader.read(BYTE_LEN)
        if len(data) == 0:
            break

        # if all nulls start a new file
        if data == b'\x00' * BYTE_LEN:
            # close old file
            writer.close()

            counter += 1
            writer = None
            writer = FileWriter("split_%d" % counter)
        else:
            print('writing %d bytes to %s' % (len(data), writer.name))
            writer.write(data)
