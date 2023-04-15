import time

import Router
import threading

class myThread (threading.Thread):
    def __init__(self, threadID, name, myrouter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.myrouter = myrouter

    def run(self):
        self.myrouter.startClient()


if __name__ == '__main__':
    myrouter1 = Router.Router('u', '127.0.0.1', 5560, '127.0.0.1', 5555)
    myrouter2 = Router.Router('x', '127.0.0.1', 5561, '127.0.0.1', 5555)
    myrouter3 = Router.Router('w', '127.0.0.1', 5562, '127.0.0.1', 5555)
    myrouter4 = Router.Router('v', '127.0.0.1', 5563, '127.0.0.1', 5555)
    myrouter5 = Router.Router('y', '127.0.0.1', 5564, '127.0.0.1', 5555)
    myrouter6 = Router.Router('z', '127.0.0.1', 5565, '127.0.0.1', 5555)
    myrouter1.doJoinFirst()
    myrouter2.doJoinFirst()
    myrouter3.doJoinFirst()
    myrouter4.doJoinFirst()
    myrouter5.doJoinFirst()
    myrouter6.doJoinFirst()
    time.sleep(5)
    thread1 = myThread(1,'r1',myrouter1)
    thread2 = myThread(2,'r2',myrouter2)
    thread3 = myThread(3,'r3',myrouter3)
    thread4 = myThread(4,'r4',myrouter4)
    thread5 = myThread(5,'r5',myrouter5)
    thread6 = myThread(6,'r6',myrouter6)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()

