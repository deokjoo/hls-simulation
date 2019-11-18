
from hls.histogram import ip_ahe


class imgFilters():
    def __init__(self, src, w, h):
        self.pipe = []
        self.pipe.append(ip_ahe(src, w, h))

    def do(self):
        for imgFilter in self.pipe:
            imgFilter.do()
    
'''
'''
if __name__ == '__main__':
    src = "/home/joo/work/eclipse/python/img/1.bin"
    
    ircam03 = imgFilters(src, src, 320, 240)
    ircam03.do()    
    