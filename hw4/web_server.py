from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    # 요청 라인의 첫 번째 줄 파싱
    request_line = req[0]
    parts = request_line.split()
    if len(parts) >= 2:
        path = parts[1]  # /index.html
        filename = path[1:]  # index.html
    else:
        filename = ''
    
    if filename == 'index.html' and os.path.exists(filename):
        # index.html 파일 전송
        f = open(filename, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        
        # HTTP 헤더
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        c.send(header.encode())
        # HTTP 바디
        c.send(data.encode())
    else:
        # 404 Not Found
        response = 'HTTP/1.1 404 Not Found\r\n\r\nNot Found'
        c.send(response.encode())
    
    c.close()