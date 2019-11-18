
from hls.imgFilters import imgFilters

'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    ircam03 = imgFilters(src, 320, 240)
    ircam03.do()    
    
