import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

print("계산기 클라이언트 시작")
print("계산식을 입력하세요. (예: 20 + 17, q: 종료)")

while True:
    # 사용자로부터 입력 받음
    expression = input("계산식 입력: ").strip()
    
    # 종료 조건
    if expression.lower() == 'q':
        print("연결을 종료합니다.")
        break
    
    # 빈 입력 무시
    if not expression:
        continue
    
    # 서버로 전송
    sock.send(expression.encode())
    
    # 서버로부터 결과 수신
    result = sock.recv(1024)
    print("결과:", result.decode())

sock.close()
