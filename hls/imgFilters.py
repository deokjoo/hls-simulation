'''
'''

from hls.dnrFilter import ip_dnr
from hls.aheFilter import ip_ahe
from hls.nucFilter import ip_nuc

'''
'''
class imgFilters():
    def __init__(self, src, w, h):
        self.pipe = []
        self.pipe.append(ip_dnr(src              , w, h))
        self.pipe.append(ip_nuc(self.pipe[-1].dst, w, h))
        self.pipe.append(ip_ahe(self.pipe[-1].dst, w, h))

    def do(self):
        for imgFilter in self.pipe:
            imgFilter.do()
    
'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    ircam03 = imgFilters(src, 320, 240)
    ircam03.do()    
    