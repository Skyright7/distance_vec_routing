import time

import Router
import threading
from configparser import ConfigParser

class myThread (threading.Thread):
    def __init__(self, threadID, name, myrouter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.myrouter = myrouter

    def run(self):
        self.myrouter.startClient()


if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.ini')
    idList = config.sections()
    n = len(idList)
    ServerIp = '127.0.0.1'
    ServerPort = 5555
    routerList = []
    for i in range(n):
        routerList.append(Router.Router(idList[i],'127.0.0.1',5560+i,ServerIp,ServerPort))
    print('Start Join')
    for j in routerList:
        j.doJoinFirst()
    time.sleep(5) # ensure all the router joined
    print('All Join finished')
    threadList = []
    for k in range(n):
        threadList.append(myThread(k,idList[k],routerList[k]))
    print('Start Updating')
    for m in threadList:
        m.start()

    for n in threadList:
        n.join()


