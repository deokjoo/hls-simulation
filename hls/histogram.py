
from hls.filter import filter
import numpy as np


'''
'''
class ip_hist():
    def __init__(self, src, dst, w, h):
        self.pading = 3
        self.kernel = self.pading * 2 + 1
                
        self.filter = filter(src, dst, w, h, 0, self.kernel, "uint16")
    '''
    '''
    def do(self):
        self.filter.method(self.st, self.op)

    '''
    opeation for pixel
    '''
    def op(self, patch):
        cur_pix = patch[0][self.pading][self.pading]
        return self.hist[cur_pix]   
    
    '''
    statitic for image
    '''
    def st(self, img  ):
        self.hist,self.index  = np.histogram(img, bins=range(16*1024))

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    dst = "/home/joo/work/eclipse/python/img/2.bin"
    
    adder = ip_hist(src, dst, 320, 240)
    adder.do()    
    
    
