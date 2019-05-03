#_*_code=utf-8_*_

#聊天室服务器端

from socket import *
import sys
import signal
import os
#send the request
def do_child(s)
    pass
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
    while True:
    
        name input('enter your name:')
        msg = 'L' + name 
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            break
        else:
            print('the user is excit')
#处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    if pid < 0:
        print('create process failed')
        return
    elif pid == 0:
        do_child(s)
    else :
        do_parent()

if __name__ == "__main__":
    main()