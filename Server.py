import Server_tabel_content
import socket
import utils

class Server:
    def __init__(self,ip, port):
        self.ip = ip
        self.port = port
        self.DV_tabel = {}
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver.bind((self.ip,self.port))
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.NoneCount = 0

    def init_add_one_to_DV_tabel(self,routerID,DV_vec):
        content = Server_tabel_content.tabel_content('',-1,DV_vec)
        self.DV_tabel[routerID] = content

    def join(self,c_ID,c_IP,c_port):
        content = self.DV_tabel[c_ID]
        content.set_ip(c_IP)
        content.set_port(c_port)
        c_pairs = content.get_pairs()
        self.sendBack(c_ID,c_IP,c_port,c_pairs,False)

    def revData(self):
        while True: # 一直收数据
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
                    if c_DV_vec != {}:
                        self.update(c_ID,c_DV_vec)
                    else:
                        if self.NoneCount < len(self.DV_tabel)-1:
                            self.NoneCount += 1
                        else:
                            break
                else:
                    self.join(c_ID, c_IP, c_port)
        self.serverDown()
        return

    def sendBack(self,from_ID,send_IP,send_port,new_pairs,update:bool):
        payload = utils.DatatoString(from_ID,send_IP,send_port,new_pairs,update)
        self.sender.sendto(payload.encode("utf-8"),(send_IP,send_port))

    def getbackway(self,c_new_pairs):
        backIDList = []
        for i,j in c_new_pairs.items():
            if j != -1:
                backIDList.append(i)
        return backIDList

    def update(self,c_ID, c_new_pairs):
        origin_content = self.DV_tabel[c_ID]
        origin_content.set_pairs(c_new_pairs)
        pushList = self.getbackway(c_new_pairs)
        for i in pushList:
            content = self.DV_tabel[i]
            back_IP = content.get_ip()
            back_port = content.get_port()
            self.sendBack(c_ID,back_IP,back_port,c_new_pairs,True)

    def serverStart(self):
        self.revData()

    def serverDown(self):
        self.sender.close()
        self.receiver.close()
        self.showDVTabel()
        return

    def showDVTabel(self):
        showString = ''
        for i,j in self.DV_tabel.items():
            showString += '\t'
            showString += str(i)
            showString += '\t'
            showString += str(j.get_ip())
            showString += '\t'
            showString += str(j.get_port())
            showString += '\t'
            showString += str(j.get_pairs())
            showString += '\t'
            showString += '\n'
        print(showString)


