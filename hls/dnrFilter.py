'''
'''
from hls.filter import filter, filterWrapper
import numpy as np


'''
samplef for filter
'''
class ip_dnr(filterWrapper):
    def __init__(self, src, w, h):
        self.dst    = src+".dnr"    
        self.t      = 3
        self.filter = filter(src, self.dst , w, h, self.t, 1, "uint16")
    
    '''
    opeation for pixel
    patch[ 1] : nxt
    patch[ 0][0][0] : current
    patch[-1] : prv
    '''
    def op(self, patch, i, y, x):
        return patch[0][0][0]
    
    '''
    statitic for image
    '''
    def st(self, img  ):
        pass

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    adder = ip_dnr(src, 320, 240)
    adder.do()    
    
    
    
    
    
    
    
    
    
    
    
    
    