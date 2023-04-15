import Server

if __name__ == '__main__':
    myserver = Server.Server('127.0.0.1', 5555)
    disvec = {'x': 5, 'w': 3, 'v': 7, 'y': -1, 'z': -1}
    myserver.init_add_one_to_DV_tabel('u', disvec)

    disvec = {'u': 5, 'w': 4, 'v': -1, 'y': 7, 'z': 9}
    myserver.init_add_one_to_DV_tabel('x', disvec)

    disvec = {'u': 3, 'x': 4, 'v': 3, 'y': 8, 'z': -1}
    myserver.init_add_one_to_DV_tabel('w', disvec)

    disvec = {'u': 7, 'x': -1, 'w': 3, 'y': 4, 'z': -1}
    myserver.init_add_one_to_DV_tabel('v', disvec)

    disvec = {'u': -1, 'x': 7, 'w': 8, 'v': 4, 'z': 2}
    myserver.init_add_one_to_DV_tabel('y', disvec)

    disvec = {'u': -1, 'x': 9, 'w': -1, 'v': -1, 'y': 2}
    myserver.init_add_one_to_DV_tabel('z', disvec)

    myserver.serverStart()