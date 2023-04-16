import Server
from configparser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.ini')
    idList = config.sections()
    myserver = Server.Server('127.0.0.1', 5555)
    for i in idList:
        c = eval(config[i]['pairs'])
        myserver.init_add_one_to_DV_tabel(i, c)

    myserver.serverStart()