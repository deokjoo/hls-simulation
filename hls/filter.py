from hls.fileIO import *

'''
https://jupiny.com/2016/09/25/decorator-class/ 
'''
class filter():
    def __init__(self, *args):
        self.src   = args[1]
        self.dst   = args[2]
        self.w     = args[3]
        self.h     = args[4]
        self.dtype = args[5]
        
        print(self.src)
    '''
    '''
    def method(self):
        with fileIOWriter(self.w, self.h, self.dst, "uint16") as wrt:
            seq = fileIOReader(self.w, self.h, self.src, "uint16")
            for img in seq:
                tmp = self.frame_op(img)
                wrt.addFrame(tmp)
    '''
    '''
    def frame_op(self, img):
        print("hello..")
        return img         

'''
 filter for kernel frame_op
'''
class filterKernel(filter):
    def __init__(self, kernel, *args):
        super().__init__(self, *args)
        
        self.kernel = kernel
        self.pading = int((self.kernel - 1) / 2)

    def frame_op(self, img):     
        dst_img = np.zeros_like(img)
        pad_img = np.pad(img, (self.pading, self.pading), 'edge')
        
        for y,x in product(range(self.h), range(self.w)):
            patch = pad_img[y:y+self.kernel, x:x+self.kernel]
            dst_img[y][x] = self.operation(patch)
          
        return dst_img  
          
    def operation(self, patch):
        return patch[self.pading][self.pading]


'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    dst = "/home/joo/work/eclipse/python/img/2.bin"
    
    adder = filterKernel(3, src, dst, 320, 240, "uint16")
    adder.method()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    