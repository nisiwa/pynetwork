from urllib.parse import quote_plus
import socket

request = "GET /index.php?title=webapi/guide/webservice-geocoding"

def geocode():
    sock = socket.socket()
    sock.connect(('lbsyun.baidu.com', 80))
    print('**********************')
    #socket.sendall(request.encode('utf-8'))
    sock.sendall(request.encode('ascii'))
    print('send over')
    raw_replay = b''
    while True:
        more = sock.recv(4096)
        print(more)
        if not more:
            break
        raw_replay += more
    print(raw_replay.decode('utf-8'))

if __name__ == '__main__':
    geocode()
