#!/usr/bin/env python
# encoding: utf-8

import argparse, socket

def recvall(sock, length):
    data = b''
    while length>len(data):
        more = sock.recv(length-len(data))
        if not more:
            raise EOFError('was excepting %d bytes but only received'
                           '%d bytes before the socket closed'%(length, len(data)))
        data += more
        return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print("listening at:", sock.getsockname())
    while True:
        print("Waiting to accept a new connection")
        sc, sockname = sock.accept()
        print("we have accept a connection from:", sockname)
        print("sock name:", sc.getsockname())
        print("sock peer:", sc.getpeername())
        message = recvall(sc, 16)
        print("incomming 16 message:", message)
        sc.sendall(b'Farewel,client')
        sc.close()
        print("replay send , socket closed")

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(b'hello server')
    print("client has been assigned socket name:", sock.getsockname())
    recv = recvall(sock, 16)
    print("server say:", recv)
    sock.close()

if __name__ == "__main__":
    choice = {"server":server, "client":client}
    parser = argparse.ArgumentParser(description="Send and receive over tcp")
    parser.add_argument('role', help='choice a role')
    parser.add_argument('host', help='interface the server listen at;'
                               'host the client send to')
    parser.add_argument('-p', metavar='PORT', default='1060', type=int, help='TCP port(default 1060)')
    args = parser.parse_args()
    function = choice[args.role]
    function(args.host, args.p)
