#_*_code=utf-8_*_

#聊天室服务器端

from socket import *
import sys
import signal
import os
#send the request
def do_child(s)
    while True:
        msg,addr = s.recvfrom(1024)
        msg = msg.decode()
        tmp = msg.split('')
#receive
def do_parent()
    pass

def main():
    if len(sys.argv)!= 3:
        print('argv error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
#处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#创建多进程
    pid = os.fork()
    if pid < 0:
        print('create process failed')
        return
    elif pid == 0:
        do_child(s)
    else :
        do_parent()

if __name__ == "__main__":
    main()