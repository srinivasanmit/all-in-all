import sys
class FileSystem(object):
 
    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices
 
print(sys.getsizeof( FileSystem ))
 
class FileSystem1(object):
 
    __slots__ = ['files', 'folders', 'devices']
    
    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices
 
print(sys.getsizeof( FileSystem1 ))
