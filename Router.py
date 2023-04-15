
# 固有属性: self.ip = ip
#         self.port = port

# 发送逻辑，接收逻辑（都分别分为Join关键字跟Update关键字）
import socket
import utils
import time

class Router:
    def __init__(self,id,ip,port,serverIP,serverPort):
        self.Id = id
        self.ip = ip
        self.port = port
        self.DV_pairs = {} # pairs的结构应该是 {routID:distance,...}(pairs初始是只有自己相邻节点有值其余全是-1)
        self.server_IP = serverIP
        self.server_port = serverPort
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver.bind((self.ip,self.port))
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.CLoseTimer = time.time()
        self.NoneCount = 0

    def join(self,c_DV_vec):
        self.DV_pairs = c_DV_vec

    def revData(self):
        while True: # 一直收数据
            data, addr = self.receiver.recvfrom(1024)
            if data != None:
                data = data.decode("utf-8")
                c_IP, c_port = addr
                # 通过自定义的解析器把数据拆分出来
                c_ID = utils.DatadeString(data)[0]
                c_DV_vec = utils.DatadeString(data)[1]
                update = utils.DatadeString(data)[2]
                if update:
                    # 这里进入DV算法主体逻辑通过收到的DV跟from_ID更新自己的DV
                    self.DV_Algorithm(c_ID,c_DV_vec)
                    # 再将信息update发回给server
                    self.sendToServer(self.Id,self.DV_pairs,True)
                else:
                    self.join(c_DV_vec)
            else:
                if self.NoneCount == 0:
                    self.CLoseTimer = time.time()
                    self.NoneCount += 1
                else:
                    dtime = time.time() - self.CLoseTimer
                    if dtime >= 5:
                        break
                    else:
                        pass
        self.client_down()

    def startClient(self):
        self.sendToServer(self.Id, self.DV_pairs, False)
        self.revData()

    def sendToServer(self,from_ID,c_DV_vec,update:bool):
        payload = utils.DatatoString(from_ID,c_DV_vec,update)
        self.sender.sendto(payload.encode("utf-8"),(self.server_IP,self.server_port))
        # 这里写发送逻辑，将对应需要发送的信息打包通过server_ip和server_port发给server

    def DV_Algorithm(self,from_id,c_DV_vec:map): # pairs的结构应该是 List[{routID:distance},]
        to_distance = self.DV_pairs[from_id]
        for key,value in c_DV_vec:
            if key == self.Id:
                pass
            else:
                dis_origin = self.DV_pairs[key]
                if dis_origin == -1:
                    # 直接更新
                    self.DV_pairs[key] = to_distance + value
                else:
                    self.DV_pairs[key] = min(dis_origin,to_distance + value)
        # self.showDV()
        return

    def client_down(self):
        self.sender.close()
        self.receiver.close()

    def showDV(self):
        print(str(self.DV_pairs))