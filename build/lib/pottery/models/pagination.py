class Pagination():
    url = 'http://localhost:5000/{}?limit={}&marker={}'
    def __init__(self,limit,marker,type):
        self.current = Pagination.url.format(type,str(limit),str(marker))
        self.previous = Pagination.url.format(type,str(limit),str(marker-1 if marker > 0 else 0))
        self.next = Pagination.url.format(type, str(limit), str(marker+1))
