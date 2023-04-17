import socket
import utils

class Router:
    def __init__(self,id,ip,port,serverIP,serverPort):
        self.Id = id
        self.ip = ip
        self.port = port
        self.DV_pairs = {}
        self.server_IP = serverIP
        self.server_port = serverPort
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver.bind((self.ip,self.port))
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.repeatCount = 0
        self.DV_before = {}

    def join(self,c_DV_vec):
        self.DV_pairs = c_DV_vec

    def revData(self):
        while True:
            data, addr = self.receiver.recvfrom(1024)
            if data != None:
                data = data.decode("utf-8")
                data = utils.DatadeString(data)
                c_ID = data[0]
                c_IP = data[1]
                c_port = data[2]
                c_DV_vec = data[3]
                update = data[4]
                if update:
                    if self.repeatCount < 25: # if the number of the router are so huge,this need to change
                        self.DV_before = self.DV_pairs
                        self.DV_Algorithm(c_ID, c_DV_vec)
                        if self.DV_before == self.DV_pairs:
                            self.repeatCount += 1
                        self.sendToServer(self.Id, self.DV_pairs, True)
                    else:
                        break
                else:
                    self.join(c_DV_vec)
        self.sendToServer(self.Id, {}, True)
        self.client_down()
        return

    def startClient(self):
        self.sendToServer(self.Id, self.DV_pairs, True)
        self.revData()

    def sendToServer(self,from_ID,c_DV_vec,update:bool):
        payload = utils.DatatoString(from_ID,self.ip,self.port,c_DV_vec,update)
        self.sender.sendto(payload.encode("utf-8"),(self.server_IP,self.server_port))

    def DV_Algorithm(self,from_id,c_DV_vec):
        to_distance = self.DV_pairs[from_id]
        for key,value in c_DV_vec.items():
            if key == self.Id:
                pass
            else:
                dis_origin = self.DV_pairs[key]
                if dis_origin == -1:
                    self.DV_pairs[key] = to_distance + value
                else:
                    if value == -1:
                        pass
                    else:
                        self.DV_pairs[key] = min(dis_origin,to_distance + value)

    def client_down(self):
        self.sender.close()
        self.receiver.close()
        return

    def showDV(self):
        print(str(self.DV_pairs))

    def doJoinFirst(self):
        self.sendToServer(self.Id, self.DV_pairs, False)
        data, addr = self.receiver.recvfrom(1024)
        if data != None:
            data = data.decode("utf-8")
            data = utils.DatadeString(data)
            c_ID = data[0]
            c_IP = data[1]
            c_port = data[2]
            c_DV_vec = data[3]
            update = data[4]
            if update:
                pass
            else:
                self.join(c_DV_vec)


