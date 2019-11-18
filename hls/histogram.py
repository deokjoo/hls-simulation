'''
'''
from hls.filter import filter, filterWrapper
import numpy as np


'''
'''
class ip_ahe(filterWrapper):
    def __init__(self, src, w, h):
        self.pading = 3
        self.kernel = self.pading * 2 + 1
                
        self.filter = filter(src, src+".ahe", w, h, 0, self.kernel, "uint16")
        
        self.hist = np.ones(((16*1024)))

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
    
    adder = ip_ahe(src, 320, 240)
    adder.do()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
