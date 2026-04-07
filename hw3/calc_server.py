import socket
import re

def parse_and_calculate(expression):
    """
    계산식을 파싱하여 계산 결과 반환
    지원: +, -, *, / (나누기는 소수점 1자리까지)
    """
    try:
        # 공백 제거
        expr = expression.replace(" ", "")
        # 정규식으로 파싱: 숫자 연산자 숫자 형태
        # 음수도 고려: -5, -10 등
        pattern = r'^(-?\d+)\s*([+\-*/])\s*(-?\d+)$'
        match = re.match(pattern, expr)
        
        if not match:
            return "에러: 잘못된 형식입니다. (예: 20 + 17)"
        
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        
        # 계산 수행
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "에러: 0으로 나눌 수 없습니다."
            result = num1 / num2
            # 소수점 1자리까지 표시
            result = round(result, 1)
        
        return f"{num1} {operator} {num2} = {result}"
    
    except Exception as e:
        return f"에러: {str(e)}"

# 서버 설정
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

print("계산기 서버 시작... 포트 9000 대기 중")

while True:
    client, addr = s.accept()
    print(f"클라이언트 연결: {addr}")
    
    try:
        while True:
            # 클라이언트로부터 계산식 수신
            expression = client.recv(1024).decode()
            
            if not expression:
                break
            
            print(f"수신한 계산식: {expression}")
            
            # 계산 수행
            result = parse_and_calculate(expression)
            
            # 결과 전송
            client.send(result.encode())
            print(f"전송 결과: {result}")
    
    except Exception as e:
        print(f"에러 발생: {str(e)}")
    
    finally:
        client.close()
        print(f"클라이언트 {addr} 연결 종료")
