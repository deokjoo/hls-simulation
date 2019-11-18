from hls.fileIO import *

'''
https://jupiny.com/2016/09/25/decorator-class/ 
'''

def default_op(patch):
    return 0
    
    
class filter():
    def __init__(self, *args):
        self.src   = args[0]
        self.dst   = args[1]
        self.w     = args[2]
        self.h     = args[3]
        self.t     = args[4]
        self.kernel= args[5]     
        self.dtype = args[6]
        
        self.pading = int((self.kernel - 1) / 2)
                
        print(self.src)
    '''
    '''
    def method(self, st, op=default_op):
        
        self.seqs = []
        
        with fileIOWriter(self.w, self.h, self.dst, "uint16") as wrt:
            src = fileIOReader(self.w, self.h, self.src, "uint16")
            
            for i, img in enumerate(src):
                if(i == 0):
                    seqs = [img] * (self.t*2+1)
                else:
                    seqs = np.roll(seqs, -1)
                    seqs[self.t] = img
                 
                '''
                for rtl sequence matching( current frame using previous frame's statistics
                '''
                wrt.addFrame(self.frame_op(seqs, op))                       
                st(img)   
    '''
    processing..
    '''
    def frame_op(self, seqs, op):     
        dst_img = np.zeros_like(seqs[0])
        
        pad_seq = [np.pad(img, (self.pading, self.pading), 'edge') for img in seqs]
        
        for y,x in product(range(self.h), range(self.w)):
            patch = [pad_img[y:y+self.kernel, x:x+self.kernel] for pad_img in pad_seq]
            dst_img[y][x] = op(patch, y, x)
          
        return dst_img  
         
'''
'''
class filterWrapper():
    def __init__(self, src, w, h):
        pass
    '''
    '''
    def do(self):
        self.filter.method(self.st, self.op)

    '''
    opeation for pixel
    '''
    def op(self, patch):
        return 0
    
    '''
    statitic for image
    '''
    def st(self, img  ):
        pass

# '''
# '''
# if __name__ == '__main__':
#     src = "/home/joo/work/eclipse/python/img/1.bin"
#     dst = "/home/joo/work/eclipse/python/img/2.bin"
#     
#     adder = filter(src, dst, 320, 240, 1, 3, "uint16")
#     adder.method()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    