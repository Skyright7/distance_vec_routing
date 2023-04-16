# 初始化逻辑跟转发的逻辑
# 维护一个表, router ID， IP， Port ，List<node,cost> pairs（这个表应该开始就直接有的）
# 为了性能，这个表实际使用哈希表的方式格式为{routerID:tabel_content}
# tabel_content具体包含ip,port,pairs三个信息
# pairs的结构应该是 List[{routID:distance},]
# 收到join之后，去表中找到这个router的信息
# 之后将发过来的pairs返回给client表示其成功注册
# 收到update之后，在表中找到这个跟这个router相邻的router，将新的消息转发过去

import Server_tabel_content
import socket
import utils

class Server:
    def __init__(self,ip, port):
        self.ip = ip
        self.port = port
        self.DV_tabel = {} # 这个结构应该是routerID:tabel_content
        # 这个tabel 会在server初始化的时候就初始化，通过读取一个ini文件
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver.bind((self.ip,self.port))
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.NoneCount = 0

    def init_add_one_to_DV_tabel(self,routerID,DV_vec):
        content = Server_tabel_content.tabel_content('',-1,DV_vec)
        self.DV_tabel[routerID] = content

    def join(self,c_ID,c_IP,c_port):
        # 因为收到join了
        # 更新DV表中port跟IP的项目
        content = self.DV_tabel[c_ID]
        content.set_ip(c_IP)
        content.set_port(c_port)
        c_pairs = content.get_pairs()
        # 这里写更新tabel之后的回发逻辑将vector发回去给对应的client,这里是原路发回
        self.sendBack(c_ID,c_IP,c_port,c_pairs,False)

    def revData(self):
        while True: # 一直收数据
            data, addr = self.receiver.recvfrom(1024)
            if data != None:
                data = data.decode("utf-8")
                print(data)
                # 通过自定义的解析器把数据拆分出来
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
                        if self.NoneCount < 5:
                            self.NoneCount += 1
                        else:
                            break
                else:
                    self.join(c_ID, c_IP, c_port)
        self.serverDown()
        return

    def sendBack(self,from_ID,send_IP,send_port,new_pairs,update:bool):
        # 通过自定义的编码器将数据表格打包成string
        payload = utils.DatatoString(from_ID,send_IP,send_port,new_pairs,update)
        # 发给要发的节点
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
        # 将这个pairs的内容回发给所有的在这个pairs中值不为-1的router(通过DVtabel来找到ip地址跟port)
        pushList = self.getbackway(c_new_pairs)
        for i in pushList:
            # 这里通过id（i）将新的vector push给这个id对应的节点
            content = self.DV_tabel[i]
            back_IP = content.get_ip()
            back_port = content.get_port()
            self.sendBack(c_ID,back_IP,back_port,c_new_pairs,True)
        # 展示每次更新情况其实可以在这个时候print
        #####

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




# if __name__ == '__main__':
#     # 传输方面测试通过
#     myserver = Server('127.0.0.1', 5555)
#     disvec = {'x': 5, 'w': 3, 'v': 7, 'y': -1, 'z': -1}
#     myserver.init_add_one_to_DV_tabel('u', disvec)
#     print(myserver.showDVTabel())
#     myserver.serverStart()