#!/usr/bin/env python
# encoding: utf-8

import socket, argparse, sys

def connect_to(host_name_or_ip):
    try:
        tpinfols = socket.getaddrinfo(host_name_or_ip, 'www', 0, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME)
    except socket.gaierror as e:
        print("Name service failure:", e.args[0])
        sys.exit(1)

    tpinfo = tpinfols[0]
    socket_args = tpinfo[:3]
    address = tpinfo[4]
    sock = socket.socket(*socket_args)
    try:
        sock.connect(address)
    except socket.error as e:
        print('Network failure:', e.args[1])
    else:
        print('Success:host', tpinfo[3], 'is listen on 80 port')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="try to connect port 80")
    parser.add_argument('hostname', help="hostname you want to connect")
    args = parser.parse_args()
    connect_to(args.hostname)
