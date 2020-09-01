##with  open('d:\\test.txt','w') as fo:
##    fo.write('Welcome ')
##    fo.write('to Beijing')
##

class MyFileOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
 
    def __enter__(self):
        self.openedFile = open(self.filename, self.mode)
        return self.openedFile
 
    def __exit__(self, *unused):
        self.openedFile.close()
 
with MyFileOpen('test.txt','w') as fo:
    fo.write('Welcome ')
    fo.write('to Beijing')
