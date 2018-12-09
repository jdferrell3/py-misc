# Script to find the end of a gzip file

# reads file in chunks and repeatedly tries to gunzip

import os
import sys
import gzip
import io

BUFF_SIZE = 8192
START = 4600000

with open(sys.argv[1], 'rb') as reader:
    counter = START  # byte counter

    # read first chunk
    data = reader.read(START)

    while True:
        # read smaller chunk
        temp = reader.read(BUFF_SIZE)
        if len(temp) == 0:
            print('End of file')
            break

        # append one byte at a time and try to gunzip
        i = 0
        while i < len(temp):
            data += bytes([temp[i]])
            fileobj = io.BytesIO(data)
            try:
                print(gzip.GzipFile(fileobj=fileobj).read())
                print(counter)  ## final offset
                sys.exit(0)
            except Exception as e:
                # print(e)
                pass
            if counter % 100000 == 0:
                print(counter)
            counter += 1
            i += 1
