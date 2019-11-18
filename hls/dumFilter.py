'''
'''
from hls.filter import filter, filterWrapper
import numpy as np


'''
samplef for filter
'''
class ip_dummmy(filterWrapper):
    def __init__(self, src, w, h):
        self.pading = 3
        self.kernel = self.pading * 2 + 1            
        self.filter = filter(src, src+".ahe", w, h, 0, self.kernel, "uint16")
    
    '''
    opeation for pixel
    patch[ 1] : nxt
    patch[ 0] : current
    patch[-1] : prv
    '''
    def op(self, patch, y, x):
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
    
    