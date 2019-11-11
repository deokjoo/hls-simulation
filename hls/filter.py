
from hls.fileIO import *

'''
'''
class filter():
    def __init__(self, src, dst, w, h, dtype):
        self.src = src
        self.dst = dst
        self.w   = w
        self.h   = h
        self.dtype = dtype
        
    '''
    '''
    def method(self):
        with fileIOWriter(self.w, self.h, self.dst, "uint16") as wrt:
            seq = fileIOReader(self.w, self.h, self.src, "uint16")
            for img in seq:
                tmp = self.method_kernel(img, 3, 3)
                wrt.addFrame(tmp)
    '''
    '''
    def method_kernel(self, img, k_col, k_row):
        print("hello..")
        return img         

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    dst = "/home/joo/work/eclipse/python/img/2.bin"
    
    adder = filter(src, dst, 320, 240, "uint16")
    adder.method()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    