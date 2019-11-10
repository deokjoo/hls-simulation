import numpy as np
from hls.fileIO import *
'''
'''

class fileIO:
    def __init__(self, w, h, name, dtype):
        self.w     = w
        self.h     = h
        self.name  = name
        self.dtype = dtype
    
        self.seqs  = self._loadFile()

    def _loadFile(self):
        tmp = np.fromfile(self.name, self.dtype).reshape(-1, self.h, self.w)
        return tmp
    
    '''
    for iteration
    '''
    def __iter__(self):
        self.index = 0
        return self
 
    def __next__(self):
        if self.index >= self.seqs.shape[0]:
            raise StopIteration
        
        n = self.seqs[self.index]
        self.index += 1
        return n    
    
    
    '''
    '''
    if __name__ == '__main__':
        src = "/home/joo/work/eclipse/python/img/1.bin"
        seq = fileIO(320, 240, src, "uint16")
        
        for img in seq:
            print(img.shape)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    