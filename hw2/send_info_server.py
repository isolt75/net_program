import socket
s = socket.socket(socket.AF_INET,
 socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
while True:
 print('Server 시작... 포트 9000 대기 중')
 client, addr = s.accept()
 print('Connection from ', addr)
 client.send(b'Hello ' + addr[0].encode())
 # 학생의 이름을 수신한 후 출력
 name = client.recv(1024)
 print("이름:", name.decode())
 # 학생의 학번을 전송
 student_id = "20211492"
 client.send(student_id.encode())

 client.close()