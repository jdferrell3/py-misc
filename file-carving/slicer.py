import os
import sys


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

if len(sys.argv) != 5:
    print('"slice" out section of file given two offsets\n')
    print("Usage:\n\t%s <begin> <end> <infile> <outfile>\n" % sys.argv[0])
    sys.exit(1)

begin = int(sys.argv[1])
end = int(sys.argv[2])
total = end - begin

with open(sys.argv[3], 'rb') as reader:
    writer = FileWriter(sys.argv[4])

    reader.seek(begin)

    data = reader.read(total)
    if len(data) == 0:
        print('Unexpected data length')
        sys.exit(1)
    else:
        print('writing %d bytes to %s' % (len(data), writer.name))
        writer.write(data)
    writer.close()
