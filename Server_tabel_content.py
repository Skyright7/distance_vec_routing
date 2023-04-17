# pairs should be {routID:distance,}
class tabel_content:
    def __init__(self,ip:str,port:int,pairs:dict):
        self.ip = ip
        self.port = port
        self.pairs = pairs

    def get_ip(self):
        return self.ip

    def set_ip(self,ip):
        self.ip = ip

    def get_port(self):
        return self.port

    def set_port(self,port):
        self.port = port

    def get_pairs(self):
        return self.pairs

    def set_pairs(self,pairs):
        self.pairs = pairs
