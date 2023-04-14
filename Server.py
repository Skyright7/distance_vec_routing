# 初始化逻辑跟转发的逻辑
# 维护一个表, router ID， IP， Port ，List<node,cost> pairs（这个表应该开始就直接有的）
# 收到join之后，去表中找到这个router的信息
# 之后将（那个list的表）返回给client
# 收到update之后，在表中找到这个跟这个router相邻的router，将新的消息转发过去

# pairs的结构应该是 List[{routID:distance},]
import Server_tabel_content

class Server:
    def __init__(self,ip, port):
        self.ip = ip
        self.port = port
        self.DV_tabel = {} # 这个结构应该是routerID:tabel_content

    def refresh_tabel(self,c_ID,c_DV_tabel):
        # 从收到的dv_tabel中解析content
        content = c_DV_tabel[c_ID]
        # 将server的contenttabel更新
        self.DV_tabel[c_ID] = content


    def join(self,c_ID,c_DV_tabel):
        # 更新server的DVtabel
        self.refresh_tabel(c_ID,c_DV_tabel)
        # 这里写更新tabel之后的回发逻辑将新的tabel发回去给client
        self.sendBack(c_ID,c_DV_tabel)

    def revData(self):
        # 这里写接收逻辑，解析出是updata还是join，然后还有DV_tabel
        c_ID,c_DV_tabel = 0,{}
        # 这里判断收到的是join逻辑还是update逻辑
        uptate = True
        if uptate:
            self.update(c_ID,c_DV_tabel)
        else:
            self.join(c_ID,c_DV_tabel)
        pass

    def sendBack(self,c_ID,c_DV_tabel):
        # 这里写回发逻辑，通过id找到port跟ip将更新过的DV_tabel发回给routerID所在
        pass

    def update(self,c_ID,c_DV_tabel):
        # 更新tabel
        self.refresh_tabel(c_ID,c_DV_tabel)
        # 将这个pairs的内容回发给所有的在这个pairs中值不为-1的router(通过DVtabel来找到ip地址跟port)
        for i in range(2):
            # 这里通过id（i）将新的tabel发回去
            self.sendBack(i,self.DV_tabel)
        # 展示每次更新情况其实可以在这个时候print
        # print(self.DV_tabel["u"].get_pairs())
        pass