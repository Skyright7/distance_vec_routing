# pairs的结构应该是 List[{routID:distance},]
class tabel_content:
    def __init__(self,ip,port,pairs):
        self.ip = ip
        self.port = port
        self.pairs = pairs

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

    def get_pairs(self):
        return self.pairs