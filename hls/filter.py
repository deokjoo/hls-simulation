
from hls.fileIO import *

'''
https://jupiny.com/2016/09/25/decorator-class/ 
'''
class filter():
#     def __init__(self, src, dst, w, h, dtype): *args
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
                tmp = self.operation(img)
                wrt.addFrame(tmp)
    '''
    '''
    def operation(self, img):
        print("hello..")
        return img         

'''
 filter for kernel operation
'''
class filterKernel(filter):
    def __init__(self, kernel, *args):
        super().__init__(self, *args)
        
        self.kernel = 3

    def operation(self, img):
        print("hello filter with padding bufffer")
        pad_img = img
        return img   


'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    dst = "/home/joo/work/eclipse/python/img/2.bin"
    
    adder = filterKernel(3, src, dst, 320, 240, "uint16")
    adder.method()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    