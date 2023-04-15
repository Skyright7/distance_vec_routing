
# 固有属性: self.ip = ip
#         self.port = port

# 发送逻辑，接收逻辑（都分别分为Join关键字跟Update关键字）

class Router:
    def __init__(self,id,ip,port):
        self.Id = id
        self.ip = ip
        self.port = port
        self.DV_pairs = {} # pairs的结构应该是 {routID:distance,...}(pairs初始是只有自己相邻节点有值其余全是-1)
        self.server_IP = '1.1.1.1'
        self.server_port = 1004
        self.repeat_count = 0 # 这个到一定值（暂定3）就认为是本路由的表更新已经完成了，断开连接

    def refresh_vec(self,from_ID,c_DV_vec,update:bool):
        if update:
            # 用收到的dv_vec来更新自己的
            if c_DV_vec == self.DV_pairs:
                self.repeat_count += 1
            else:
                # 这里进入DV算法主体逻辑通过收到的DV跟from_ID更新自己的DV
                self.DV_Algorithm(from_ID,c_DV_vec)
                # DV更新完成后将更新好的新的DV用update标识再发回server（迭代）
                pass
        # 收到join这里就什么都不做
        if self.repeat_count > 3:
            # 这里写断开连接的逻辑
            pass


    def join(self,c_ID,c_DV_vec):
        self.sendToServer(c_ID,c_DV_vec,False)

    def revData(self):
        # 这里写接收逻辑，解析出是updata还是join，然后还有DV_vec
        from_ID,c_DV_vec = 'u',{}
        # 这里判断收到的是join逻辑还是update逻辑(假设是update)
        uptate = True
        self.refresh_vec(from_ID,c_DV_vec,uptate)
        pass

    def sendToServer(self,from_ID,c_DV_vec,update:bool):
        # 这里写发送逻辑，将对应需要发送的信息打包通过server_ip和server_port发给server
        pass

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
        return