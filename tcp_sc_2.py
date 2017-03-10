#!/usr/bin/env python
# encoding: utf-8

import sys, socket, argparse

def server(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print("listening at", sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        n = 0
        print("processing up to 1024 bytes at a time form", sockname)
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode("ascii").upper().encode("ascii")
            sc.sendall(output)
            n += len(data)
            print("\r%d bytes processed so far" %(n,), end=" ")
            #sys.stdout.flush()
        print()
        sc.close()
        print("server closed")

def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount+15)//16*16
    message = b'capitalize this!'

    print('send bytes', bytecount)
    sock.connect((host, port))
    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print("\r %d bytes sent" %(sent, ), end=" ")
        sys.stdout.flush()
    print()
    sock.shutdown(socket.SHUT_WR)

    print("receiving all the data the server send back")

    received = 0
    while True:
        data = sock.recv(42)
        if not received:
            print('the first received data say:', repr(data))
        if not data:
            break
        received += len(data)
        print("\r %d bytes received"%(received, ), end=' ')
        #sys.stdout.flush()
    print()

if __name__ == "__main__":
    choices = {'server':server, 'client':client}
    parser = argparse.ArgumentParser(description="get deadlocked over tcp")
    parser.add_argument('role', choices=choices, help='choice a role')
    parser.add_argument('host', help='host input')
    parser.add_argument('bytecount', type=int, default=16, nargs="?", help="number of bytes for client to send")
    parser.add_argument('-p', type=int, default=8888, metavar='PORT', help='tcp port(default 8888)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.bytecount)
