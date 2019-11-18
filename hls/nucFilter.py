'''
'''
from hls.filter import filter, filterWrapper
import numpy as np


'''
samplef for filter
'''
class ip_nuc(filterWrapper):
    def __init__(self, src, w, h):
        self.dst    =  src+".nuc"        
        self.filter = filter(src, self.dst, w, h, 0, 1, "uint16")
        
        '''
        private
        '''
        self.coeff = np.fromfile("./coeff/nuc.coeff",dtype="uint32").reshape(h, w)
        
    '''
    opeation for pixel
    '''
    def op(self, patch, i, y, x):
        gain = int((self.coeff[y][x] >> 16) & 0xFFFF)
        off  = int((self.coeff[y][x] >>  0) & 0xFFFF)
        cur = patch[0][0][0]
          
        nuc = int(cur * gain / 1024) + off 
        
        return nuc
    
    '''
    statitic for image
    '''
    def st(self, img  ):
        pass

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    adder = ip_nuc(src, 320, 240)
    adder.do()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    