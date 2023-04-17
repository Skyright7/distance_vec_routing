# Project 3: Distance Vector Routing Algorithm
## Environment
my personal python environment is Python 3.9.10.
But I do not use the specific feature. So, the python version just over 3 is ok.
I recommended running this code on a python 3.6 above.

## How to run the code
You need two terminal. For we have server and router, two character.
On the first Terminal you run the command:
```shell
python ServerStarter.py
```
Please make Sure that you start the server first. This is important.
Then you can run the command:
```shell
python RouterStarter.py
```
This will use multi-thread to start all the router in parallel.

Then the final result tabel will show on the server's terminal.

## If you want change
### about the .ini file
if you want to change the router's data or the router's number.
You can just adjust the config.ini file in the root directory.
### about the port
The port using in this project is
for server: 5555
for router, it will base on .ini file's data. It will base on the
router's number to automatically using the port number start from 5560.
For example, if I have 3 router in the ini file, my router's port will be 5560,5561,5562.

If you want to change the router number or the IP number(default '127.0.0.1' Your local IP)
You need go the ServerStarter.py and the RouterStarter.py to change it by yourself.

