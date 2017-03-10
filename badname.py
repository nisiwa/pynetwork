#!/usr/bin/env python
# encoding: utf-8

from urllib.parse import quote
import socket
import json

request_text = """\
GET /geocoder/v2/?address={}&output=json&ak={} HTTP/1.1\r\n\
Host:api.map.baidu.com:80\r\n\
User-Agent:badname.py\r\n\
Connection:close\r\n\
\r\n
"""

def geocode(address):
    sock = socket.socket()
    sock.connect(('api.map.baidu.com', 80))
    print('**********************')
    request = request_text.format(quote(address), 'ZIhr931pcZwO3sDhCPkAvnUUvrIMXUIn')
    #socket.sendall(request.encode('utf-8'))
    sock.sendall(request.encode('ascii'))
    print('send over')
    raw_replay = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_replay += more
    print(raw_replay.decode('utf-8'))

if __name__ == '__main__':
    geocode('北京')
