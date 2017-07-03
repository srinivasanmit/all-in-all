#!/usr/bin/python 

import os
import sys
import time

def make_files(folder='test',filename='1', size='1'):
    retry = 3
    while retry:
        try:
            os.makedirs(folder)
            break
        except Exception as e:
            print "retrying folder create...\n"
            retry = retry - 1
            if retry <= 0:
                print "Reached max retry to create folder, Error:{0}".format(str(e))
#                raise e
        
    filepath = "{0}/{1}".format(folder, filename)
    with open(filepath, "w") as fd:
        fd.seek(size - 1)
        fd.write("\0")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: rec_dir <Root folders> <Nested folder> <File Size>\n"
        sys.exit(1)
    rootFolderCount = int(sys.argv[1])
    subFolderCount = int(sys.argv[2])
    fileSize = int(sys.argv[3])

    for i in xrange(rootFolderCount):
        for j in xrange(subFolderCount):
            subFolder = "P-{0}{1}/sub{2}".format(i, time.time(), time.time())
            make_files(subFolder, 'f-{0}'.format(time.time()), fileSize)
     
    
    
