'''
'''
from hls.filter import filter, filterWrapper
import numpy as np


'''
samplef for filter
'''
class ip_dummmy(filterWrapper):
    def __init__(self, src, w, h):
        self.dst    =  src+".dum"    
        self.pading = 3
        self.kernel = self.pading * 2 + 1 
        self.t      = 3           
        self.filter = filter(src, self.dst , w, h, self.t, self.kernel, "uint16")
    
    '''
    opeation for pixel
    patch[ 1] : nxt
    patch[ 0][0][0] : current
    patch[-1] : prv
    '''
    def op(self, patch, i, y, x):
        return 0 
    
    '''
    statitic for image
    '''
    def st(self, img  ):
        pass

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    adder = ip_dummmy(src, 320, 240)
    adder.do()    
    
    