# 初始化逻辑跟转发的逻辑
# 维护一个表, router ID， IP， Port ，List<node,cost> pairs（这个表应该开始就直接有的）
# 为了性能，这个表实际使用哈希表的方式格式为{routerID:tabel_content}
# tabel_content具体包含ip,port,pairs三个信息
# pairs的结构应该是 List[{routID:distance},]
# 收到join之后，去表中找到这个router的信息
# 之后将发过来的pairs返回给client表示其成功注册
# 收到update之后，在表中找到这个跟这个router相邻的router，将新的消息转发过去

import Server_tabel_content

class Server:
    def __init__(self,ip, port):
        self.ip = ip
        self.port = port
        self.DV_tabel = {} # 这个结构应该是routerID:tabel_content

    def refresh_tabel(self,c_ID,c_IP,c_port,c_new_pairs):
        content = Server_tabel_content.tabel_content(c_IP,c_port,c_new_pairs)
        self.DV_tabel[c_ID] = content

# join逻辑好像可以直接优化掉
    # def join(self,c_ID,c_IP,c_port,c_new_pairs):
    #     # 更新server的DVtabel
    #     self.refresh_tabel(c_ID,c_IP,c_port,c_new_pairs)
    #     # 这里写更新tabel之后的回发逻辑将vector发回去给对应的client,这里是原路发回
    #     self.sendBack(c_ID,c_IP,c_port,c_new_pairs,False)

    def revData(self):
        # 这里写接收逻辑，解析出是updata还是join，然后还有DV_vec
        # ip跟port可以通过解析得到，
        c_ID,c_IP,c_port,c_DV_vec,update = 'u','1.1.1.1',1004,[],True
        # 这里判断收到的是join逻辑还是update逻辑 假设是update
        # 不管是update还是join,先更新更新server的DV_tabel
        self.refresh_tabel(c_ID, c_IP, c_port, c_DV_vec)
        if update:
            self.update(c_ID,c_DV_vec)
        else:
            self.sendBack(c_ID,c_IP,c_port,c_DV_vec,update)
        pass

    def sendBack(self,from_ID,send_IP,send_port,new_pairs,update:bool):
        # 实际传输的数据只有 id,c_new_pairs,update:bool这三个打包发给send_IP,send_port对应的router
        # 感觉可以起一个统一的tostring方法还有deString方法
        # 这里写回发逻辑
        # 用upd吧(就是打包加回发逻辑)
        pass

    def getbackway(self,c_new_pairs):
        backIDList = []
        for i in c_new_pairs:
            if i.values() != -1:
                backIDList.append(i.keys())
        return backIDList

    def update(self,c_ID,c_new_pairs):
        # 将这个pairs的内容回发给所有的在这个pairs中值不为-1的router(通过DVtabel来找到ip地址跟port)
        pushList = self.getbackway(c_new_pairs)
        for i in pushList:
            # 这里通过id（i）将新的vector push给这个id对应的节点
            content = self.DV_tabel[i]
            back_IP = content.get_ip()
            back_port = content.get_port()
            self.sendBack(c_ID,back_IP,back_port,c_new_pairs,True)
        # 展示每次更新情况其实可以在这个时候print
        # print(self.DV_tabel["u"].get_pairs())
        pass