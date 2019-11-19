'''
'''
import numpy as np
import cv2
from itertools import * 
from hls.fileIO import *

'''
class for binary file reader
'''
class fileIOReader:
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
class for binary file reader
'''
class fileIOWriter:
    def __init__(self, w, h, name, dtype, fps= 1, video = True):
        self.w     = w
        self.h     = h
        self.name  = name
        self.dtype = dtype
        self.seq   = []
        self.fps   = fps
        self.video = video
        
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self._save()
        
    '''
    '''    
    def addFrame(self, img):
        self.seq.append(img)
    
    '''
    '''  
    def _save(self):
        '''
        check whether list is empty..
        '''
        np.stack(self.seq).astype(self.dtype).tofile(self.name)
        if self.video:
            self._saveVideo(self.name, self.seq)
        
     
    def _saveVideo(self, name, seq):   
        # initialize video writer
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        out = cv2.VideoWriter(name+".avi", fourcc, self.fps, (self.w,self.h))
        
        for i in range(0,len(seq)):
            gray = cv2.normalize(seq[i], None, 255, 0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            gray_3c = cv2.merge([gray, gray, gray])
            out.write(gray_3c)
        
        out.release()       
        
        
        
        
        
        
        
    
'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    dst = "/home/joo/work/eclipse/python/img/2.bin"
    
    with fileIOWriter(320, 240, dst, "uint16") as wrt:
        seq = fileIOReader(320, 240, src, "uint16")
        for img in seq:
            wrt.addFrame(img)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    