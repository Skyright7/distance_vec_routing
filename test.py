import Router
import Server
import _thread

if __name__ == '__main__':
    myserver = Server.Server('127.0.0.1',5555)
    # id,ip,port,serverIP,serverPort
    myrouter1 = Router.Router('u','127.0.0.1',5560,'127.0.0.1',5555)
    disvec = {'x':5,'w':3,'v':7,'y':-1,'z':-1}
    myserver.init_add_one_to_DV_tabel('u',disvec)
    myrouter2 = Router.Router('x', '127.0.0.1', 5561, '127.0.0.1', 5555)
    disvec = {'u':5,'w':4,'v':-1,'y':7,'z':9}
    myserver.init_add_one_to_DV_tabel('x',disvec)
    myrouter3 = Router.Router('w', '127.0.0.1', 5562, '127.0.0.1', 5555)
    disvec = {'u':3,'x':4,'v':3,'y':8,'z':-1}
    myserver.init_add_one_to_DV_tabel('w',disvec)
    myrouter4 = Router.Router('v', '127.0.0.1', 5563, '127.0.0.1', 5555)
    disvec = {'u':7,'x':-1,'w':3,'y':4,'z':-1}
    myserver.init_add_one_to_DV_tabel('v',disvec)
    myrouter5 = Router.Router('y', '127.0.0.1', 5564, '127.0.0.1', 5555)
    disvec = {'u':-1,'x':7,'w':8,'v':4,'z':2}
    myserver.init_add_one_to_DV_tabel('y',disvec)
    myrouter6 = Router.Router('z', '127.0.0.1', 5565, '127.0.0.1', 5555)
    disvec = {'u':-1,'x':9,'w':-1,'v':-1,'y':2}
    myserver.init_add_one_to_DV_tabel('z',disvec)
    _thread.start_new_thread(myserver.serverStart())
    _thread.start_new_thread(myrouter1.startClient())
    _thread.start_new_thread(myrouter2.startClient())
    _thread.start_new_thread(myrouter3.startClient())
    _thread.start_new_thread(myrouter4.startClient())
    _thread.start_new_thread(myrouter5.startClient())
    _thread.start_new_thread(myrouter6.startClient())